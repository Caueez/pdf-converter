from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def download_file(self, bucket_name, object_name, file_path): ...

    @abstractmethod
    def generate_presigned_url(self, object_name, expiration=3600): ...