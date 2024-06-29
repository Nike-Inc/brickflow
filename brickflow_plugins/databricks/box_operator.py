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
# Clear existing handlers
if logger.hasHandlers():
    logger.handlers.clear()
# Add stream handler
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
    """
    A base class that provides methods for authenticating to Box.
    """

    def __init__(self, **kwargs):
        self.logger = logger
        self.secret_scope = kwargs.get("secret_scope")
        self.cerberus_client_url = kwargs.get("cerberus_client_url")
        if not self.secret_scope:
            raise ValueError("secret_scope is required")
        self.client = self.box_authentication()

    def box_authentication(self):
        """
        Authenticate with Box using JWT authentication.
        Logs details of the authentication process.
        """
        try:
            auth_options = self.get_box_connection(
                self.secret_scope, self.cerberus_client_url
            )
            auth = JWTAuth(**auth_options)
            self.logger.info("Successfully authenticated with Box using JWT.")
            return Client(auth)
        except Exception as e:
            self.logger.error(f"Error in Box authentication: {e}")
            raise

    def get_cerberus_dtl(self, cerebrus_cred_path, cerberus_client_url):
        """
        Get credentials from Cerberus.
        :return: returns username and password from the provided Cerberus key.
        Logs details of the credential retrieval process.
        """
        self.logger.info("Reading Cerberus credentials")
        from cerberus.client import CerberusClient

        cerberus_client = CerberusClient(cerberus_client_url)
        try:
            creds = cerberus_client.get_secrets_data(cerebrus_cred_path)
            self.logger.info("Successfully retrieved credentials from Cerberus.")
            return creds
        except Exception as e:
            self.logger.error(f"Error getting Cerberus credentials: {e}")
            raise

    def get_box_dbutils_dtl(self, secret_scope):
        """
        Get credentials from dbutils.
        :param secret_scope: scope for accessing secrets.
        :return: returns auth_options from the provided dbutils key.
        Logs details of the credential retrieval process.
        """
        self.logger.info("Reading Box dbutils credentials")
        if secret_scope.startswith("app/"):
            secret_scope = secret_scope.replace("app/", "", 1)
        elif secret_scope.startswith("shared/"):
            secret_scope = secret_scope.replace("shared/", "", 1)
        try:
            auth_options = {
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
            self.logger.info("Successfully retrieved credentials from dbutils.")
            return auth_options
        except Exception as e:
            self.logger.error(f"Error getting dbutils credentials: {e}")
            raise

    def get_box_cerberus_dtl(self, secret_scope, cerberus_client_url):
        """
        Get credentials from Cerberus.
        :param secret_scope: scope for accessing secrets.
        :param cerberus_client_url: URL for the Cerberus client.
        :return: returns auth_options from the provided Cerberus key.
        Logs details of the credential retrieval process.
        """
        self.logger.info("Reading Box Cerberus credentials")
        try:
            box_creds = self.get_cerberus_dtl(secret_scope, cerberus_client_url)
            auth_options = {
                "client_id": box_creds["client_id"],
                "client_secret": box_creds["client_secret"],
                "jwt_key_id": box_creds["jwt_key_id"],
                "rsa_private_key_data": box_creds["rsa_private_key_data"].encode(
                    "utf-8"
                ),
                "rsa_private_key_passphrase": box_creds["rsa_private_key_passphrase"],
                "enterprise_id": box_creds["enterprise_id"],
            }
            self.logger.info("Successfully retrieved credentials from Cerberus.")
            return auth_options
        except Exception as e:
            self.logger.error(f"Error getting Cerberus credentials: {e}")
            raise

    def get_box_connection(self, secret_scope, cerberus_client_url):
        """
        Get connection details for Box authentication.
        :param secret_scope: scope for accessing secrets.
        :param cerberus_client_url: URL for the Cerberus client.
        :return: returns auth_options for Box authentication.
        Logs details of the connection retrieval process.
        """
        try:
            auth_options = self.get_box_dbutils_dtl(secret_scope)
            self.logger.info(
                "Successfully obtained Box connection details from dbutils."
            )
            return auth_options
        except Exception:
            if cerberus_client_url:
                self.logger.info(
                    "Failed to get credentials from dbutils, trying Cerberus."
                )
                try:
                    auth_options = self.get_box_cerberus_dtl(
                        secret_scope, cerberus_client_url
                    )
                    self.logger.info(
                        "Successfully obtained Box connection details from Cerberus."
                    )
                    return auth_options
                except Exception as e:
                    self.logger.error(
                        f"Error getting credentials from both dbutils and Cerberus: {e}"
                    )
                    raise
            else:
                self.logger.error(
                    "Cerberus client URL not provided, cannot retrieve credentials from Cerberus."
                )
                raise Exception("Cerberus client URL not provided.")


class BoxToVolumesOperator(BoxAuthenticator):
    """
    A class that provides methods to download files from a Box folder to a local volume.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.folder_id = kwargs.get("folder_id")
        self.volume_path = kwargs.get("volume_path")
        self.file_names = kwargs.get("file_names", [])
        self.file_id = kwargs.get("file_id")
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
            list: A list of items in the folder.
        """
        self.logger.info(
            f"Attempting to retrieve items from Box folder with ID: {folder_id}"
        )
        try:
            items = self.client.folder(folder_id).get_items()
            items_list = [
                item for item in items
            ]  # Convert generator to list to count items
            self.logger.info(
                f"Successfully retrieved {len(items_list)} items from Box folder ID: {folder_id}"
            )
            return items_list
        except BoxAPIException as e:
            self.logger.error(
                f"Box API error while retrieving items from folder ID {folder_id}: {e}"
            )
            raise
        except Exception as e:
            self.logger.error(
                f"Unexpected error while retrieving items from folder ID {folder_id}: {e}"
            )
            raise

    def download_folder(self, folder_id, volume_path):
        """
        Download the contents of a Box folder, including subfolders, to a local volume.
        Args:
            folder_id (str): The ID of the Box folder.
            volume_path (str): The path to the local volume.
        """
        items = self.client.folder(folder_id).get_items()
        for item in items:
            if item.type == "file":
                self.download_file(item, volume_path)
            elif item.type == "folder":
                # Create a subfolder in the volume path for the Box folder
                subfolder_path = os.path.join(volume_path, item.name)
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)
                self.download_folder(item.id, subfolder_path)

    def download_file(self, item, volume_path):
        """
        Download a file from Box to a local volume.
        Args:
            item (BoxItem): The Box item to download.
            volume_path (str): The path to the local volume.
        Logs details of the file download process.
        """
        self.logger.info(f"Downloading file {item.name} to {volume_path}")
        try:
            with open(os.path.join(volume_path, item.name), "wb") as output_file:
                self.client.file(item.id).download_to(output_file)
            self.logger.info(f"{item.name} successfully downloaded to {volume_path}")
        except BoxAPIException as e:
            self.logger.error(f"Box API error during file download: {e}")
            raise
        except IOError as e:
            self.logger.error(f"File IO error during download: {e}")
            raise

    def execute(self):
        """
        Download files from a Box folder to a local volume based on the specified criteria.
        If file_id or file_names is specified, download only those files.
        If neither is specified, download all files in the folder.
        Logs details of the download process.
        """
        self.logger.info(
            f"Starting download from Box folder ID {self.folder_id} to {self.volume_path}"
        )
        try:
            if self.file_id or self.file_names:
                items = self.get_items(self.folder_id)
                for item in items:
                    if item.type == "file":
                        # Download by file_id if specified
                        if self.file_id and item.id == self.file_id:
                            self.download_file(item, self.volume_path)
                        # Download by file_names if specified
                        elif self.file_names and item.name in self.file_names:
                            self.download_file(item, self.volume_path)
            else:
                # Download all files and folders if neither file_id nor file_names is specified
                self.download_folder(self.folder_id, self.volume_path)
        except BoxAPIException as e:
            self.logger.error(f"Box API error during download: {e}")
            raise
        except IOError as e:
            self.logger.error(f"File IO error during download: {e}")
            raise


class VolumesToBoxOperator(BoxAuthenticator):
    """
    A class for uploading files from a local volume to a Box folder.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.folder_id = kwargs.get("folder_id")
        self.volume_path = kwargs.get("volume_path")
        self.file_names = kwargs.get("file_names", [])
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
            str or None: The ID of the existing file, or None if the file does not exist.
        Logs details of the file ID retrieval process.
        """
        self.logger.info(
            f"Checking if file {file_name} exists in Box folder ID {folder_id}"
        )
        try:
            items = self.client.folder(folder_id).get_items()
            for item in items:
                if item.name == file_name and item.type == "file":
                    self.logger.info(f"File {file_name} found with ID {item.id}")
                    return item.id
            self.logger.info(f"File {file_name} not found in Box folder ID {folder_id}")
            return None
        except BoxAPIException as e:
            self.logger.error(f"Box API error while checking for existing file: {e}")
            raise

    def get_existing_folder_id(self, parent_folder_id, folder_name):
        """
        Get the ID of an existing folder in a Box folder.
        Args:
            parent_folder_id (str): The ID of the parent Box folder.
            folder_name (str): The name of the folder.
        Returns:
            str or None: The ID of the existing folder, or None if the folder does not exist.
        Logs details of the folder ID retrieval process.
        """
        self.logger.info(
            f"Checking if folder {folder_name} exists in Box folder ID {parent_folder_id}"
        )
        try:
            items = self.client.folder(parent_folder_id).get_items()
            for item in items:
                if item.name == folder_name and item.type == "folder":
                    self.logger.info(f"Folder {folder_name} found with ID {item.id}")
                    return item.id
            self.logger.info(
                f"Folder {folder_name} not found in Box folder ID {parent_folder_id}"
            )
            return None
        except BoxAPIException as e:
            self.logger.error(f"Box API error while checking for existing folder: {e}")
            raise

    def upload_file(self, folder_id, file_path):
        file_name = os.path.basename(file_path)
        self.logger.info(f"Uploading file {file_name} to Box folder ID {folder_id}")
        try:
            existing_file_id = self.get_existing_file_id(folder_id, file_name)
            if existing_file_id:
                self.update_file(existing_file_id, file_path)
            else:
                self.client.folder(folder_id).upload(file_path)
            self.logger.info(
                f"Successfully uploaded {file_name} to Box folder ID {folder_id}"
            )
        except BoxAPIException as e:
            self.logger.error(f"Box API error during file upload: {e}")
            raise
        except IOError as e:
            self.logger.error(f"File IO error during upload: {e}")
            raise

    def update_file(self, file_id, file_path):
        """
        Update the contents of a file in a Box folder.
        Args:
            file_id (str): The ID of the file.
            file_path (str): The path to the updated file.
        Logs details of the file update process.
        """
        if not os.path.isfile(file_path):
            self.logger.error(f"Provided path {file_path} is not a file.")
            return

        file_name = os.path.basename(file_path)
        self.logger.info(f"Updating file {file_name} in Box with ID {file_id}")
        try:
            with open(file_path, "rb") as file_stream:
                self.client.file(file_id).update_contents_with_stream(file_stream)
            self.logger.info(
                f"Successfully updated {file_name} in Box with ID {file_id}"
            )
        except BoxAPIException as e:
            self.logger.error(f"Box API error during file update: {e}")
            raise
        except IOError as e:
            self.logger.error(f"File IO error during update: {e}")
            raise

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
        try:
            folder = self.client.folder(parent_folder_id).create_subfolder(folder_name)
            self.logger.info(
                f"Successfully created folder {folder_name} with ID {folder.id}"
            )
            return folder.id
        except BoxAPIException as e:
            self.logger.error(f"Box API error during folder creation: {e}")
            raise

    def upload_folder(self, parent_folder_id, local_folder_path):
        """
        Upload the contents of a local folder to a Box folder recursively.
        Args:
            parent_folder_id (str): The ID of the Box folder where the contents will be uploaded.
            local_folder_path (str): The path to the local folder.
        """
        folder_name = os.path.basename(local_folder_path)
        existing_folder_id = self.get_existing_folder_id(parent_folder_id, folder_name)
        if existing_folder_id:
            new_folder_id = existing_folder_id
        else:
            new_folder_id = self.create_folder(parent_folder_id, folder_name)

        for item in os.listdir(local_folder_path):
            item_path = os.path.join(local_folder_path, item)
            if os.path.isdir(item_path):
                self.upload_folder(new_folder_id, item_path)
            else:
                self.upload_file(new_folder_id, item_path)

    def execute(self):
        """
        Upload files from a local volume to a Box folder.
        If file_names is specified, only those files will be uploaded.
        If file_names is not specified, all files in the volume will be uploaded.
        Logs details of the upload process.
        """
        self.logger.info(
            f"Starting upload to Box folder ID {self.folder_id} from {self.volume_path}"
        )
        try:
            # Determine which files and folders to upload
            items_to_upload = (
                self.file_names if self.file_names else os.listdir(self.volume_path)
            )

            for item in items_to_upload:
                item_path = os.path.join(self.volume_path, item)
                if os.path.isdir(item_path):
                    self.upload_folder(self.folder_id, item_path)
                elif os.path.isfile(item_path):
                    self.upload_file(self.folder_id, item_path)
                else:
                    self.logger.warning(
                        f"Path {item_path} is neither a file nor a directory."
                    )
        except BoxAPIException as e:
            self.logger.error(f"Box API error during upload: {e}")
            raise
        except IOError as e:
            self.logger.error(f"File IO error during upload: {e}")
            raise


class BoxOperator(BoxAuthenticator):
    """
    A class that provides methods for authenticating, downloading, and uploading to Box.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.folder_id = kwargs.get("folder_id")
        self.volume_path = kwargs.get("volume_path")
        self.file_names = kwargs.get("file_names", [])
        self.file_id = kwargs.get("file_id")
        self.operation = kwargs.get("operation")
        if not self.folder_id or not self.volume_path or not self.operation:
            raise ValueError(
                "folder_id, volume_path and operation (downlaod or upload) are required"
            )
        if isinstance(self.file_names, str):
            self.file_names = [self.file_names]

    def execute(self):
        """
        Execute the specified operation ('download' or 'upload').

        This method uses the class attributes to perform the desired operation on files stored in Box.
        Logs details of the execution process.
        """

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
            )
            uploader.execute()
        else:
            self.logger.error(f"Invalid operation: {self.operation}")
            raise ValueError(f"Invalid operation: {self.operation}")
