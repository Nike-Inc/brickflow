import os
import shutil
import tempfile
import unittest
from unittest.mock import MagicMock, Mock, patch

from boxsdk import Client, JWTAuth

from brickflow_plugins.databricks.box_operator import (
    BoxAuthenticator,
    BoxOperator,
    BoxOperatorException,
    BoxToVolumesOperator,
    VolumesToBoxOperator,
)


class TestBoxAuthenticator(unittest.TestCase):
    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    def test_get_box_dbutils_dtl(
        self, mock_jwt_authenticate_instance, mock_jwt_auth, mock_ctx
    ):
        # Arrange
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        # Act
        authenticator = BoxAuthenticator(
            secret_scope="test_scope", cerberus_client_url="test_url"
        )
        result = authenticator.get_box_dbutils_dtl("test_scope")
        # Assert
        self.assertEqual(result["client_id"], "client_id_value")
        self.assertEqual(result["client_secret"], "client_secret_value")
        self.assertEqual(result["jwt_key_id"], "jwt_key_id_value")
        self.assertEqual(
            result["rsa_private_key_data"], "rsa_private_key_data_value".encode("utf-8")
        )
        self.assertEqual(
            result["rsa_private_key_passphrase"], "rsa_private_key_passphrase_value"
        )
        self.assertEqual(result["enterprise_id"], "enterprise_id_value")

    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    def test_get_box_cerberus_dtl(
        self,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
    ):
        # Arrange
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value",
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Act
        authenticator = BoxAuthenticator(
            secret_scope="test_scope", cerberus_client_url="test_url"
        )
        result = authenticator.get_box_cerberus_dtl("test_scope", "test_url")

        # Assert
        self.assertEqual(result["client_id"], "client_id_value")
        self.assertEqual(result["client_secret"], "client_secret_value")
        self.assertEqual(result["jwt_key_id"], "jwt_key_id_value")
        self.assertEqual(
            result["rsa_private_key_data"], "rsa_private_key_data_value".encode("utf-8")
        )
        self.assertEqual(
            result["rsa_private_key_passphrase"], "rsa_private_key_passphrase_value"
        )
        self.assertEqual(result["enterprise_id"], "enterprise_id_value")

    @patch.object(BoxAuthenticator, "get_box_dbutils_dtl")
    @patch.object(BoxAuthenticator, "get_box_cerberus_dtl")
    @patch.object(JWTAuth, "__init__", return_value=None)
    def test_box_authentication_fails(
        self, mock_jwt_auth, mock_get_box_cerberus_dtl, mock_get_box_dbutils_dtl
    ):
        # Arrange
        mock_get_box_dbutils_dtl.side_effect = Exception("dbutils exception")
        mock_get_box_cerberus_dtl.side_effect = Exception("cerberus exception")
        _ = mock_jwt_auth
        # Act & Assert
        with self.assertRaises(BoxOperatorException):
            BoxAuthenticator(secret_scope="test_scope", cerberus_client_url="test_url")

    def test_missing_secret_scope(self):
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            BoxAuthenticator(cerberus_client_url="test_url")
        self.assertEqual(str(context.exception), "secret_scope is required")

    @patch.object(BoxAuthenticator, "get_box_dbutils_dtl")
    def test_missing_cerberus_client_url(self, mock_get_box_dbutils_dtl):
        # Arrange
        mock_get_box_dbutils_dtl.side_effect = Exception("dbutils exception")
        # Act & Assert
        with self.assertRaises(BoxOperatorException) as context:
            BoxAuthenticator(secret_scope="test_scope")
        self.assertEqual(str(context.exception), "Cerberus client URL not provided.")


class TestBoxToVolumesOperator(unittest.TestCase):
    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    def setUp(
        self,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value",
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        self.jwt_auth = JWTAuth()
        self.jwt_auth._access_token = "dummy_access_token"  # Mock access token
        self.operator = BoxToVolumesOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=tempfile.mkdtemp(),
        )
        self.operator.client = Client(self.jwt_auth)
        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

    def tearDown(self):
        # Clean up the temporary directory after each test
        shutil.rmtree(self.operator.volume_path)

    def test_get_items(self):
        # Arrange
        folder_id = "123"
        file1 = Mock(type="file", id="1")
        file1.name = "file1.txt"
        file2 = Mock(type="file", id="2")
        file2.name = "file2.txt"
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([file1, file2])
        folder_mock = Mock()
        folder_mock.get_items.return_value = items_mock
        self.operator.client.folder = Mock(return_value=folder_mock)

        # Act
        items = self.operator.get_items(folder_id)

        # Assert
        self.operator.client.folder.assert_called_once_with(folder_id)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].name, "file1.txt")
        self.assertEqual(items[1].name, "file2.txt")

    def test_download_file(self):
        # Arrange
        file_item = Mock(type="file", id="123")
        file_item.name = "file1.txt"
        file_content = b"Test file content"
        file_mock = Mock()
        file_mock.download_to.side_effect = lambda f: f.write(file_content)
        self.operator.client.file = Mock(return_value=file_mock)

        # Act
        self.operator.download_file(file_item, self.operator.volume_path)

        # Assert
        with open(os.path.join(self.operator.volume_path, "file1.txt"), "rb") as f:
            self.assertEqual(f.read(), file_content)

    def test_download_folder(self):
        # Arrange
        folder_id = "123"
        folder_name = "test_folder"
        file_name = "file1.txt"
        file_content = b"Test file content"

        file_item = Mock(type="file", id="1")
        file_item.name = file_name
        folder_item = Mock(type="folder", id="2")
        folder_item.name = folder_name
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([file_item, folder_item])
        folder_mock = Mock()
        folder_mock.get_items.return_value = items_mock
        self.operator.client.folder = Mock(return_value=folder_mock)
        file_mock = Mock()
        file_mock.download_to.side_effect = lambda f: f.write(file_content)
        self.operator.client.file = Mock(return_value=file_mock)

        # Act
        self.operator.download_folder(folder_id, self.operator.volume_path)

        # Assert
        with open(os.path.join(self.operator.volume_path, file_name), "rb") as f:
            self.assertEqual(f.read(), file_content)
        subfolder_path = os.path.join(self.operator.volume_path, folder_name)
        self.assertTrue(os.path.exists(subfolder_path))

    def test_execute_download_files_by_name(self):
        # Arrange
        self.operator.file_names = ["file1.txt", "file2.txt"]
        file1 = Mock(type="file", id="123")
        file1.name = "file1.txt"
        file2 = Mock(type="file", id="456")
        file2.name = "file2.txt"
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([file1, file2])
        folder_mock = Mock()
        folder_mock.get_items.return_value = items_mock
        self.operator.client.folder = Mock(return_value=folder_mock)
        file_mock = Mock()
        file_mock.download_to.side_effect = lambda f: f.write(b"Test file content")
        self.operator.client.file = Mock(return_value=file_mock)

        # Act
        self.operator.execute()

        # Assert
        with (
            open(os.path.join(self.operator.volume_path, "file1.txt"), "rb") as f1,
            open(os.path.join(self.operator.volume_path, "file2.txt"), "rb") as f2,
        ):
            self.assertEqual(f1.read(), b"Test file content")
            self.assertEqual(f2.read(), b"Test file content")

    def test_execute_download_files_by_id(self):
        # Arrange
        self.operator.file_id = "123"
        file1 = Mock(type="file", id="123")
        file1.name = "file1.txt"
        file2 = Mock(type="file", id="456")
        file2.name = "file2.txt"
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([file1, file2])
        folder_mock = Mock()
        folder_mock.get_items.return_value = items_mock
        self.operator.client.folder = Mock(return_value=folder_mock)
        file_mock = Mock()
        file_mock.download_to.side_effect = lambda f: f.write(b"Test file content")
        self.operator.client.file = Mock(return_value=file_mock)

        # Act
        self.operator.execute()

        # Assert
        with open(os.path.join(self.operator.volume_path, "file1.txt"), "rb") as f1:
            self.assertEqual(f1.read(), b"Test file content")
        self.assertFalse(
            os.path.exists(os.path.join(self.operator.volume_path, "file2.txt"))
        )

    def test_execute_download_files_by_pattern(self):
        # Arrange
        self.operator.file_pattern = ".txt"
        file1 = Mock(type="file", id="123")
        file1.name = "file1.txt"
        file2 = Mock(type="file", id="456")
        file2.name = "file2.log"
        file3 = Mock(type="file", id="789")
        file3.name = "file3.txt"
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([file1, file2, file3])
        folder_mock = Mock()
        folder_mock.get_items.return_value = items_mock
        self.operator.client.folder = Mock(return_value=folder_mock)
        file_mock = Mock()
        file_mock.download_to.side_effect = lambda f: f.write(b"Test file content")
        self.operator.client.file = Mock(return_value=file_mock)

        # Act
        self.operator.execute()

        # Assert
        with (
            open(os.path.join(self.operator.volume_path, "file1.txt"), "rb") as f1,
            open(os.path.join(self.operator.volume_path, "file3.txt"), "rb") as f3,
        ):
            self.assertEqual(f1.read(), b"Test file content")
            self.assertEqual(f3.read(), b"Test file content")
        self.assertFalse(
            os.path.exists(os.path.join(self.operator.volume_path, "file2.log"))
        )

    def test_execute_download_all_files(self):
        # Arrange
        file1 = Mock(type="file", id="123")
        file1.name = "file1.txt"
        file2 = Mock(type="file", id="456")
        file2.name = "file2.txt"
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([file1, file2])
        folder_mock = Mock()
        folder_mock.get_items.return_value = items_mock
        self.operator.client.folder = Mock(return_value=folder_mock)
        file_mock = Mock()
        file_mock.download_to.side_effect = lambda f: f.write(b"Test file content")
        self.operator.client.file = Mock(return_value=file_mock)

        # Act
        self.operator.execute()

        # Assert
        with (
            open(os.path.join(self.operator.volume_path, "file1.txt"), "rb") as f1,
            open(os.path.join(self.operator.volume_path, "file2.txt"), "rb") as f2,
        ):
            self.assertEqual(f1.read(), b"Test file content")
            self.assertEqual(f2.read(), b"Test file content")

    def test_execute_download_folders(self):
        # Arrange
        self.operator.file_names = None
        folder1 = Mock(type="folder", id="789")
        folder1.name = "folder1"
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([folder1])
        folder_mock = Mock()
        folder_mock.get_items.return_value = items_mock
        self.operator.client.folder = Mock(return_value=folder_mock)

        # Act
        self.operator.execute()

        # Assert
        folder_path = os.path.join(self.operator.volume_path, "folder1")
        self.assertTrue(os.path.exists(folder_path))


class TestVolumesToBoxOperator(unittest.TestCase):
    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    def setUp(
        self,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        self.jwt_auth = JWTAuth()
        self.jwt_auth._access_token = "dummy_access_token"  # Mock access token
        self.temp_dir = tempfile.mkdtemp()
        self.operator = VolumesToBoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
        )
        self.operator.client = Client(self.jwt_auth)
        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

    def tearDown(self):
        # Clean up the temporary directory after each test
        shutil.rmtree(self.temp_dir)

    @patch.object(Client, "folder")
    def test_execute_upload_with_file_names(self, mock_folder):
        # Arrange
        self.operator.file_names = ["file1.txt", "file2.txt"]
        _ = mock_folder

        # Create mock files in the temporary directory
        for file_name in self.operator.file_names:
            with open(
                os.path.join(self.temp_dir, file_name), "w", encoding="utf-8"
            ) as f:
                f.write("Test content")

        # Mock Box folder upload method
        folder_mock = Mock()
        self.operator.client.folder = Mock(return_value=folder_mock)
        folder_mock.upload.side_effect = lambda file_path: None

        # Mock get_items to return an iterable
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([])
        folder_mock.get_items.return_value = items_mock

        # Act
        self.operator.execute()

        # Assert
        upload_calls = [call[0][0] for call in folder_mock.upload.call_args_list]
        self.assertIn(os.path.join(self.temp_dir, "file1.txt"), upload_calls)
        self.assertIn(os.path.join(self.temp_dir, "file2.txt"), upload_calls)
        self.assertEqual(len(upload_calls), 2)
        self.assertEqual(len(self.operator.uploaded_files), 2)
        self.assertIn("file1.txt", self.operator.uploaded_files)
        self.assertIn("file2.txt", self.operator.uploaded_files)

    @patch.object(Client, "folder")
    def test_execute_upload_with_file_pattern(self, mock_folder):
        # Arrange
        self.operator.file_pattern = ".txt"
        _ = mock_folder

        # Create mock files in the temporary directory
        with open(os.path.join(self.temp_dir, "file1.txt"), "w", encoding="utf-8") as f:
            f.write("Test content")
        with open(os.path.join(self.temp_dir, "file2.log"), "w", encoding="utf-8") as f:
            f.write("Test content")

        # Mock Box folder upload method
        folder_mock = Mock()
        self.operator.client.folder = Mock(return_value=folder_mock)
        folder_mock.upload.side_effect = lambda file_path: None

        # Mock get_items to return an iterable
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([])
        folder_mock.get_items.return_value = items_mock

        # Act
        self.operator.execute()

        # Assert
        folder_mock.upload.assert_called_once_with(
            os.path.join(self.temp_dir, "file1.txt")
        )
        self.assertEqual(len(self.operator.uploaded_files), 1)
        self.assertIn("file1.txt", self.operator.uploaded_files)

    @patch.object(Client, "folder")
    def test_execute_upload_all_files(self, mock_folder):
        # Arrange
        _ = mock_folder
        # Create mock files and folders in the temporary directory
        with open(os.path.join(self.temp_dir, "file1.txt"), "w", encoding="utf-8") as f:
            f.write("Test content")
        os.makedirs(os.path.join(self.temp_dir, "subfolder"))
        with open(
            os.path.join(self.temp_dir, "subfolder", "file2.txt"), "w", encoding="utf-8"
        ) as f:
            f.write("Test content")

        # Mock Box folder upload method
        folder_mock = Mock()
        self.operator.client.folder = Mock(return_value=folder_mock)
        folder_mock.upload.side_effect = lambda file_path: None
        folder_mock.create_subfolder.side_effect = lambda folder_name: Mock(
            id="subfolder_id"
        )

        # Mock get_items to return an iterable
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([])
        folder_mock.get_items.return_value = items_mock

        # Act
        self.operator.execute()

        # Assert
        folder_mock.upload.assert_any_call(os.path.join(self.temp_dir, "file1.txt"))
        folder_mock.create_subfolder.assert_called_once_with("subfolder")
        self.assertEqual(
            len(self.operator.uploaded_files), 2
        )  # Expecting 2 files uploaded now
        self.assertIn("file1.txt", self.operator.uploaded_files)
        self.assertIn("file2.txt", self.operator.uploaded_files)

    @patch.object(Client, "folder")
    def test_execute_upload_no_files(self, mock_folder):
        # Arrange
        self.operator.file_names = ["non_existent_file.txt"]
        _ = mock_folder

        # Mock Box folder upload method
        folder_mock = Mock()
        self.operator.client.folder = Mock(return_value=folder_mock)

        # Mock get_items to return an iterable
        items_mock = MagicMock()
        items_mock.__iter__.return_value = iter([])
        folder_mock.get_items.return_value = items_mock

        # Act
        self.operator.execute()

        # Assert
        folder_mock.upload.assert_not_called()
        self.assertEqual(len(self.operator.uploaded_files), 0)


class TestBoxOperator(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.temp_dir = None

    def tearDown(self):
        # Clean up the temporary directory after each test
        if hasattr(self, "temp_dir"):
            shutil.rmtree(self.temp_dir)

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    @patch.object(BoxToVolumesOperator, "execute")
    def test_execute_download_with_file_names(
        self,
        mock_execute,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        operator = BoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
            file_names=["file1.txt", "file2.txt"],
            operation="download",
        )
        operator.client = Client(JWTAuth())

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Act
        operator.execute()

        # Assert
        mock_execute.assert_called_once()

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    @patch.object(BoxToVolumesOperator, "execute")
    def test_execute_download_with_file_id(
        self,
        mock_execute,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        operator = BoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
            file_id="123",
            operation="download",
        )
        operator.client = Client(JWTAuth())

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Act
        operator.execute()

        # Assert
        mock_execute.assert_called_once()

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    @patch.object(BoxToVolumesOperator, "execute")
    def test_execute_download_with_file_pattern(
        self,
        mock_execute,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        operator = BoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
            file_pattern=".txt",
            operation="download",
        )
        operator.client = Client(JWTAuth())

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Act
        operator.execute()

        # Assert
        mock_execute.assert_called_once()

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    @patch.object(BoxToVolumesOperator, "execute")
    def test_execute_download_all_files(
        self,
        mock_execute,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        operator = BoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
            operation="download",
        )
        operator.client = Client(JWTAuth())

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Act
        operator.execute()

        # Assert
        mock_execute.assert_called_once()

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    @patch.object(VolumesToBoxOperator, "execute")
    def test_execute_upload_with_file_names(
        self,
        mock_execute,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        operator = BoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
            file_names=["file1.txt", "file2.txt"],
            operation="upload",
        )
        operator.client = Client(JWTAuth())

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Create mock files in the temporary directory
        for file_name in operator.file_names:
            with open(
                os.path.join(self.temp_dir, file_name), "w", encoding="utf-8"
            ) as f:
                f.write("Test content")

        # Act
        operator.execute()

        # Assert
        mock_execute.assert_called_once()

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    @patch.object(VolumesToBoxOperator, "execute")
    def test_execute_upload_with_file_pattern(
        self,
        mock_execute,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        operator = BoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
            file_pattern=".txt",
            operation="upload",
        )
        operator.client = Client(JWTAuth())

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Create mock files in the temporary directory
        file_names = ["file1.txt", "file2.log", "file3.txt"]
        for file_name in file_names:
            with open(
                os.path.join(self.temp_dir, file_name), "w", encoding="utf-8"
            ) as f:
                f.write("Test content")

        # Act
        operator.execute()

        # Assert
        mock_execute.assert_called_once()

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    @patch.object(VolumesToBoxOperator, "execute")
    def test_execute_upload_all_files(
        self,
        mock_execute,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        operator = BoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
            operation="upload",
        )
        operator.client = Client(JWTAuth())

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Create mock files and folders in the temporary directory
        file_names = ["file1.txt", "file2.log", "file3.txt"]
        for file_name in file_names:
            with open(
                os.path.join(self.temp_dir, file_name), "w", encoding="utf-8"
            ) as f:
                f.write("Test content")

        subfolder_path = os.path.join(self.temp_dir, "subfolder")
        os.makedirs(subfolder_path)
        with open(
            os.path.join(subfolder_path, "file4.txt"), "w", encoding="utf-8"
        ) as f:
            f.write("Test content")

        # Act
        operator.execute()

        # Assert
        mock_execute.assert_called_once()

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    def test_invalid_operation(
        self,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Arrange
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        operator = BoxOperator(
            secret_scope="test_scope",
            cerberus_client_url="test_url",
            folder_id="test_folder_id",
            volume_path=self.temp_dir,
            operation="invalid_operation",
        )

        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            operator.execute()
        self.assertEqual(str(context.exception), "Invalid operation: invalid_operation")

    @patch("brickflow_plugins.databricks.box_operator.ctx", new_callable=MagicMock)
    @patch("cerberus.client.CerberusClient.get_secrets_data")
    @patch("cerberus.client.CerberusClient.__init__", return_value=None)
    @patch.object(JWTAuth, "__init__", return_value=None)
    @patch.object(JWTAuth, "authenticate_instance", return_value=None)
    def test_missing_required_arguments(
        self,
        mock_jwt_authenticate_instance,
        mock_jwt_auth,
        mock_cerberus_init,
        mock_get_secrets_data,
        mock_ctx,
    ):
        # Missing folder_id
        self.temp_dir = tempfile.mkdtemp()
        mock_ctx.dbutils = MagicMock()
        _ = mock_jwt_authenticate_instance
        _ = mock_jwt_auth
        _ = mock_cerberus_init

        mock_ctx.dbutils.secrets.get.side_effect = lambda scope, key: f"{key}_value"
        mock_get_secrets_data.return_value = {
            "client_id": "client_id_value",
            "client_secret": "client_secret_value",
            "jwt_key_id": "jwt_key_id_value",
            "rsa_private_key_data": "rsa_private_key_data_value".encode("utf-8"),
            "rsa_private_key_passphrase": "rsa_private_key_passphrase_value",
            "enterprise_id": "enterprise_id_value",
        }
        with self.assertRaises(ValueError) as context:
            BoxOperator(
                secret_scope="test_scope",
                cerberus_client_url="test_url",
                volume_path=self.temp_dir,
                operation="download",
            )
        self.assertEqual(
            str(context.exception),
            "folder_id, volume_path and operation (download or upload) are required",
        )

        # Missing volume_path
        with self.assertRaises(ValueError) as context:
            BoxOperator(
                secret_scope="test_scope",
                cerberus_client_url="test_url",
                folder_id="test_folder_id",
                operation="download",
            )
        self.assertEqual(
            str(context.exception),
            "folder_id, volume_path and operation (download or upload) are required",
        )

        # Missing operation
        with self.assertRaises(ValueError) as context:
            BoxOperator(
                secret_scope="test_scope",
                cerberus_client_url="test_url",
                folder_id="test_folder_id",
                volume_path=self.temp_dir,
            )
        self.assertEqual(
            str(context.exception),
            "folder_id, volume_path and operation (download or upload) are required",
        )
