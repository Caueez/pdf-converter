from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    async def create_presigned_url(self, bucket_name: str): ...