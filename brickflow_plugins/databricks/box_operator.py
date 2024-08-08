import os
import logging

try:
    from boxsdk import Client, JWTAuth, BoxAPIException
except ImportError:
    raise ImportError(
        """You must install boxsdk library to use run boxsdk plugins, please add - 'boxsdk' library either
         at project level in entrypoint or at workflow level or at task level. Examples shown below 
        entrypoint:
            with Project( ... 
                          libraries=[PypiTaskLibrary(package="boxsdk==3.9.2")]
                          ...)
        workflow:
            wf=Workflow( ...
                         libraries=[PypiTaskLibrary(package="boxsdk==3.9.2")]
                         ...)
        Task:
            @wf.task(Library=[PypiTaskLibrary(package="boxsdk==3.9.2")]
            def BoxOperator(*args):
                ...
        """
    )

try:
    from brickflow import ctx
except ImportError:
    raise ImportError(
        "plugin requires brickflow context , please install library at cluster/workflow/task level"
    )

# Set up logging
logger = logging.getLogger("Box Operator")
logger.setLevel(logging.DEBUG)
if logger.hasHandlers():
    logger.handlers.clear()
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class BoxOperatorException(Exception):
    """Custom exception class for Box Operator errors."""

    pass


class BoxOperatorTimeOutException(TimeoutError):
    """Custom exception class for Box Operator timeouts."""

    pass


class BoxAuthenticator:
    """A base class that provides methods for authenticating to Box."""

    def __init__(self, **kwargs):
        """
        Initialize the BoxAuthenticator with the given parameters.

        Args:
            secret_scope (str): The scope for secret management.
            cerberus_client_url (str): The URL for Cerberus client.
        """
        self.logger = logger
        self.secret_scope = kwargs.get("secret_scope")
        self.cerberus_client_url = kwargs.get("cerberus_client_url")
        if not self.secret_scope:
            raise ValueError("secret_scope is required")
        self.client = self.box_authentication()

    def box_authentication(self):
        """
        Authenticate with Box using JWT authentication.

        Returns:
            Client: An authenticated Box client.
        """
        auth_options = self.get_box_connection(
            self.secret_scope, self.cerberus_client_url
        )
        auth = JWTAuth(**auth_options)
        self.logger.info("Successfully authenticated with Box using JWT.")
        return Client(auth)

    def get_box_connection(self, secret_scope, cerberus_client_url):
        """
        Get connection details for Box authentication.

        Args:
            secret_scope (str): The scope for secret management.
            cerberus_client_url (str): The URL for Cerberus client.

        Returns:
            dict: A dictionary containing Box authentication details.

        Raises:
            BoxOperatorException: If credentials cannot be retrieved.
        """
        try:
            return self.get_box_dbutils_dtl(secret_scope)
        except Exception as e:
            self.logger.info(f"Failed to get credentials from dbutils: {e}")
            if cerberus_client_url:
                try:
                    return self.get_box_cerberus_dtl(secret_scope, cerberus_client_url)
                except Exception as e:
                    self.logger.error(f"Failed to get credentials from Cerberus: {e}")
                    raise BoxOperatorException(
                        "Failed to get credentials from both dbutils and Cerberus"
                    )
            else:
                self.logger.error("Cerberus client URL not provided.")
                raise BoxOperatorException("Cerberus client URL not provided.")

    def get_box_dbutils_dtl(self, secret_scope):
        """
        Get credentials from dbutils.

        Args:
            secret_scope (str): The scope for secret management.

        Returns:
            dict: A dictionary containing Box authentication details.
        """
        self.logger.info("Reading Box dbutils credentials")
        if secret_scope.startswith("app/"):
            secret_scope = secret_scope.replace("app/", "", 1)
        elif secret_scope.startswith("shared/"):
            secret_scope = secret_scope.replace("shared/", "", 1)
        return {
            "client_id": ctx.dbutils.secrets.get(secret_scope, "client_id"),
            "client_secret": ctx.dbutils.secrets.get(secret_scope, "client_secret"),
            "jwt_key_id": ctx.dbutils.secrets.get(secret_scope, "jwt_key_id"),
            "rsa_private_key_data": ctx.dbutils.secrets.get(
                secret_scope, "rsa_private_key_data"
            ).encode("utf-8"),
            "rsa_private_key_passphrase": ctx.dbutils.secrets.get(
                secret_scope, "rsa_private_key_passphrase"
            ),
            "enterprise_id": ctx.dbutils.secrets.get(secret_scope, "enterprise_id"),
        }

    def get_box_cerberus_dtl(self, secret_scope, cerberus_client_url):
        """
        Get credentials from Cerberus.

        Args:
            secret_scope (str): The scope for secret management.
            cerberus_client_url (str): The URL for Cerberus client.

        Returns:
            dict: A dictionary containing Box authentication details.
        """
        self.logger.info("Reading Box Cerberus credentials")
        from cerberus.client import CerberusClient

        cerberus_client = CerberusClient(cerberus_client_url)
        creds = cerberus_client.get_secrets_data(secret_scope)
        return {
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
            "jwt_key_id": creds["jwt_key_id"],
            "rsa_private_key_data": creds["rsa_private_key_data"].encode("utf-8"),
            "rsa_private_key_passphrase": creds["rsa_private_key_passphrase"],
            "enterprise_id": creds["enterprise_id"],
        }


class BoxToVolumesOperator(BoxAuthenticator):
    """A class that provides methods to download files from a Box folder to a local volume."""

    def __init__(self, **kwargs):
        """
        Initialize the BoxToVolumesOperator with the given parameters.

        Args:
            folder_id (str): The ID of the Box folder.
            volume_path (str): The local volume path.
            file_names (list): List of file names to download.
            file_id (str): The ID of a specific file to download.
            file_pattern (str): The pattern to match file names.
        """
        super().__init__(**kwargs)
        self.folder_id = kwargs.get("folder_id")
        self.volume_path = kwargs.get("volume_path")
        self.file_names = kwargs.get("file_names", [])
        self.file_id = kwargs.get("file_id")
        self.file_pattern = kwargs.get("file_pattern")
        self.downloaded_files = []  # To keep track of downloaded files
        if not self.folder_id or not self.volume_path:
            raise ValueError("folder_id and volume_path are required")
        if isinstance(self.file_names, str):
            self.file_names = [self.file_names]

    def get_items(self, folder_id):
        """
        Retrieve items from a Box folder.

        Args:
            folder_id (str): The ID of the Box folder.

        Returns:
            list: A list of items in the Box folder.
        """
        self.logger.info(
            f"Attempting to retrieve items from Box folder with ID: {folder_id}"
        )
        items = self.client.folder(folder_id).get_items()
        items_list = [item for item in items]
        self.logger.info(
            f"Successfully retrieved {len(items_list)} items from Box folder ID: {folder_id}"
        )
        return items_list

    def download_folder(self, folder_id, volume_path):
        """
        Download the contents of a Box folder, including subfolders, to a local volume.

        Args:
            folder_id (str): The ID of the Box folder.
            volume_path (str): The local volume path.
        """
        items = self.client.folder(folder_id).get_items()
        for item in items:
            if item.type == "file":
                self.download_file(item, volume_path)
            elif item.type == "folder":
                subfolder_path = os.path.join(volume_path, item.name)
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)
                self.download_folder(item.id, subfolder_path)

    def download_file(self, item, volume_path):
        """
        Download a file from Box to a local volume.

        Args:
            item (Item): The Box item to download.
            volume_path (str): The local volume path.
        """
        self.logger.info(f"Downloading file {item.name} to {volume_path}")
        with open(os.path.join(volume_path, item.name), "wb") as output_file:
            self.client.file(item.id).download_to(output_file)
        self.logger.info(f"{item.name} successfully downloaded to {volume_path}")
        self.downloaded_files.append(item.name)

    def execute(self):
        """
        Download files from a Box folder to a local volume based on the specified criteria.
        """
        self.logger.info(
            f"Starting download from Box folder ID {self.folder_id} to {self.volume_path}"
        )
        try:
            items = self.get_items(self.folder_id)
            for item in items:
                if item.type == "file":
                    if self.file_id and item.id == self.file_id:
                        self.download_file(item, self.volume_path)
                    elif self.file_names and item.name in self.file_names:
                        self.download_file(item, self.volume_path)
                    elif self.file_pattern and (
                        item.name.startswith(self.file_pattern)
                        or item.name.endswith(self.file_pattern)
                    ):
                        self.download_file(item, self.volume_path)
                    elif (
                        not self.file_id
                        and not self.file_names
                        and not self.file_pattern
                    ):
                        self.download_file(item, self.volume_path)
                elif (
                    item.type == "folder"
                    and not self.file_id
                    and not self.file_names
                    and not self.file_pattern
                ):
                    subfolder_path = os.path.join(self.volume_path, item.name)
                    if not os.path.exists(subfolder_path):
                        os.makedirs(subfolder_path)
                    self.download_folder(item.id, subfolder_path)
            if not self.downloaded_files:
                self.logger.info("No files were downloaded.")
            else:
                self.logger.info(f"Downloaded files: {self.downloaded_files}")
        except BoxAPIException as e:
            self.logger.error(f"Box API error during download: {e}")
            raise BoxOperatorException(f"Box API error during download: {e}")
        except IOError as e:
            self.logger.error(f"File IO error during download: {e}")
            raise BoxOperatorException(f"File IO error during download: {e}")


class VolumesToBoxOperator(BoxAuthenticator):
    """A class for uploading files from a local volume to a Box folder."""

    def __init__(self, **kwargs):
        """
        Initialize the VolumesToBoxOperator with the given parameters.

        Args:
            folder_id (str): The ID of the Box folder.
            volume_path (str): The local volume path.
            file_names (list): List of file names to upload.
            file_pattern (str): The pattern to match file names.
        """
        super().__init__(**kwargs)
        self.folder_id = kwargs.get("folder_id")
        self.volume_path = kwargs.get("volume_path")
        self.file_names = kwargs.get("file_names", [])
        self.file_pattern = kwargs.get("file_pattern")
        self.uploaded_files = []  # To keep track of uploaded files
        if not self.folder_id or not self.volume_path:
            raise ValueError("folder_id and volume_path are required")
        if isinstance(self.file_names, str):
            self.file_names = [self.file_names]

    def get_existing_file_id(self, folder_id, file_name):
        """
        Get the ID of an existing file in a Box folder.

        Args:
            folder_id (str): The ID of the Box folder.
            file_name (str): The name of the file.

        Returns:
            str: The ID of the existing file, or None if not found.
        """
        self.logger.info(
            f"Checking if file {file_name} exists in Box folder ID {folder_id}"
        )
        items = self.client.folder(folder_id).get_items()
        for item in items:
            if item.name == file_name and item.type == "file":
                self.logger.info(f"File {file_name} found with ID {item.id}")
                return item.id
        self.logger.info(f"File {file_name} not found in Box folder ID {folder_id}")
        return None

    def get_existing_folder_id(self, parent_folder_id, folder_name):
        """
        Get the ID of an existing folder in a Box folder.

        Args:
            parent_folder_id (str): The ID of the parent Box folder.
            folder_name (str): The name of the folder.

        Returns:
            str: The ID of the existing folder, or None if not found.
        """
        self.logger.info(
            f"Checking if folder {folder_name} exists in Box folder ID {parent_folder_id}"
        )
        items = self.client.folder(parent_folder_id).get_items()
        for item in items:
            if item.name == folder_name and item.type == "folder":
                self.logger.info(f"Folder {folder_name} found with ID {item.id}")
                return item.id
        self.logger.info(
            f"Folder {folder_name} not found in Box folder ID {parent_folder_id}"
        )
        return None

    def upload_file(self, folder_id, file_path):
        """
        Upload a file to a Box folder.

        Args:
            folder_id (str): The ID of the Box folder.
            file_path (str): The local file path.
        """
        file_name = os.path.basename(file_path)
        self.logger.info(f"Uploading file {file_name} to Box folder ID {folder_id}")
        existing_file_id = self.get_existing_file_id(folder_id, file_name)
        if existing_file_id:
            self.update_file(existing_file_id, file_path)
        else:
            self.client.folder(folder_id).upload(file_path)
        self.logger.info(
            f"Successfully uploaded {file_name} to Box folder ID {folder_id}"
        )
        self.uploaded_files.append(file_name)

    def update_file(self, file_id, file_path):
        """
        Update the contents of a file in a Box folder.

        Args:
            file_id (str): The ID of the file in Box.
            file_path (str): The local file path.
        """
        file_name = os.path.basename(file_path)
        self.logger.info(f"Updating file {file_name} in Box with ID {file_id}")
        with open(file_path, "rb") as file_stream:
            self.client.file(file_id).update_contents_with_stream(file_stream)
        self.logger.info(f"Successfully updated {file_name} in Box with ID {file_id}")

    def create_folder(self, parent_folder_id, folder_name):
        """
        Create a folder in Box.

        Args:
            parent_folder_id (str): The ID of the parent Box folder.
            folder_name (str): The name of the new folder.

        Returns:
            str: The ID of the created folder.
        """
        self.logger.info(
            f"Creating folder {folder_name} in Box parent folder ID {parent_folder_id}"
        )
        folder = self.client.folder(parent_folder_id).create_subfolder(folder_name)
        self.logger.info(
            f"Successfully created folder {folder_name} with ID {folder.id}"
        )
        return folder.id

    def upload_folder(self, parent_folder_id, local_folder_path):
        """
        Upload the contents of a local folder to a Box folder recursively.

        Args:
            parent_folder_id (str): The ID of the parent Box folder.
            local_folder_path (str): The local folder path.
        """
        folder_name = os.path.basename(local_folder_path)
        existing_folder_id = self.get_existing_folder_id(parent_folder_id, folder_name)
        new_folder_id = (
            existing_folder_id
            if existing_folder_id
            else self.create_folder(parent_folder_id, folder_name)
        )

        for item in os.listdir(local_folder_path):
            item_path = os.path.join(local_folder_path, item)
            if os.path.isdir(item_path):
                self.upload_folder(new_folder_id, item_path)
            else:
                self.upload_file(new_folder_id, item_path)

    def execute(self):
        """
        Upload files from a local volume to a Box folder.
        """
        self.logger.info(
            f"Starting upload to Box folder ID {self.folder_id} from {self.volume_path}"
        )
        try:
            items_to_upload = set(self.file_names) if self.file_names else set()
            all_items = os.listdir(self.volume_path)
            if self.file_names:
                for item in self.file_names:
                    item_path = os.path.join(self.volume_path, item)
                    if os.path.isfile(item_path):
                        items_to_upload.add(item)
                    else:
                        self.logger.warning(
                            f"File {item} specified in file_names does not exist in volume path."
                        )
            if self.file_pattern:
                for item in all_items:
                    if os.path.isfile(os.path.join(self.volume_path, item)):
                        if item.startswith(self.file_pattern) or item.endswith(
                            self.file_pattern
                        ):
                            items_to_upload.add(item)
            if not self.file_names and not self.file_pattern:
                for item in all_items:
                    item_path = os.path.join(self.volume_path, item)
                    if os.path.isfile(item_path):
                        items_to_upload.add(item)
                    elif os.path.isdir(item_path):
                        self.upload_folder(self.folder_id, item_path)
            for item in items_to_upload:
                item_path = os.path.join(self.volume_path, item)
                if os.path.isfile(item_path):
                    self.upload_file(self.folder_id, item_path)
                else:
                    self.logger.warning(
                        f"Path {item_path} is not a file and will be skipped."
                    )
            if not self.uploaded_files:
                self.logger.info("No files were uploaded.")
            else:
                self.logger.info(f"Uploaded files: {self.uploaded_files}")
        except BoxAPIException as e:
            self.logger.error(f"Box API error during upload: {e}")
            raise BoxOperatorException(f"Box API error during upload: {e}")
        except IOError as e:
            self.logger.error(f"File IO error during upload: {e}")
            raise BoxOperatorException(f"File IO error during upload: {e}")


class BoxOperator(BoxAuthenticator):
    """A class that provides methods for authenticating, downloading, and uploading to Box."""

    def __init__(self, **kwargs):
        """
        Initialize the BoxOperator with the given parameters.

        Args:
            folder_id (str): The ID of the Box folder.
            volume_path (str): The local volume path.
            file_names (list): List of file names to download/upload.
            file_id (str): The ID of a specific file to download.
            file_pattern (str): The pattern to match file names.
            operation (str): The operation to perform ('download' or 'upload').
        """
        super().__init__(**kwargs)
        self.folder_id = kwargs.get("folder_id")
        self.volume_path = kwargs.get("volume_path")
        self.file_names = kwargs.get("file_names", [])
        self.file_id = kwargs.get("file_id")
        self.file_pattern = kwargs.get("file_pattern")
        self.operation = kwargs.get("operation")
        if not self.folder_id or not self.volume_path or not self.operation:
            raise ValueError(
                "folder_id, volume_path and operation (download or upload) are required"
            )
        if isinstance(self.file_names, str):
            self.file_names = [self.file_names]

    def execute(self):
        """
        Execute the specified operation ('download' or 'upload').

        Raises:
            ValueError: If the operation is invalid.
            BoxOperatorException: If the operation fails.
        """
        try:
            if self.operation == "download":
                self.logger.info(
                    f"Downloading files {self.file_names} from Box folder {self.folder_id} to volume {self.volume_path}"
                )
                downloader = BoxToVolumesOperator(
                    secret_scope=self.secret_scope,
                    cerberus_client_url=self.cerberus_client_url,
                    folder_id=self.folder_id,
                    volume_path=self.volume_path,
                    file_names=self.file_names,
                    file_id=self.file_id,
                    file_pattern=self.file_pattern,
                )
                downloader.execute()
            elif self.operation == "upload":
                self.logger.info(
                    f"Uploading files {self.file_names} to Box folder {self.folder_id} from volume {self.volume_path}"
                )
                uploader = VolumesToBoxOperator(
                    secret_scope=self.secret_scope,
                    cerberus_client_url=self.cerberus_client_url,
                    folder_id=self.folder_id,
                    volume_path=self.volume_path,
                    file_names=self.file_names,
                    file_pattern=self.file_pattern,
                )
                uploader.execute()
            else:
                self.logger.error(f"Invalid operation: {self.operation}")
                raise ValueError(f"Invalid operation: {self.operation}")
        except BoxOperatorException as e:
            self.logger.error(f"Failed to execute operation: {e}")
            raise
