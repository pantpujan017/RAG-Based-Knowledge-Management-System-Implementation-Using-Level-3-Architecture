# services/azure_storage_service.py  (rename this file)
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential
import os
from config import Config

class AzureStorage:
    def __init__(self):
        self.config = self._get_config()
        self.blob_service_client = BlobServiceClient(
            account_url=f"https://{self.config['account_name']}.blob.core.windows.net",
            credential=DefaultAzureCredential()
        )
        self.container_name = self.config['container_name']
        self._ensure_container_exists()

    def _get_config(self):
        return {
            'account_name': os.getenv("AZURE_STORAGE_ACCOUNT"),
            'container_name': os.getenv("AZURE_STORAGE_CONTAINER", "knowledge-base")
        }

    def _ensure_container_exists(self):
        try:
            container_client = self.blob_service_client.get_container_client(self.container_name)
            if not container_client.exists():
                container_client.create_container()
        except AzureError as e:
            print(f"Container error: {e}")

    def upload_file(self, file_obj, filename):
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name, blob=filename
            )
            file_obj.seek(0)
            blob_client.upload_blob(file_obj, overwrite=True)
            return True
        except AzureError as e:
            print(f"Upload error: {e}")
            return False

    def get_file(self, filename):
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name, blob=filename
            )
            return blob_client.download_blob().readall()
        except AzureError:
            return None