from abc import ABC, abstractmethod


class HttpInterface(ABC):
    @abstractmethod
    async def get(self, url: str) -> dict: ...

    @abstractmethod
    async def post(self, url: str, data: dict) -> dict: ...

    @abstractmethod
    async def put(self, url: str, data: dict) -> dict: ...

    @abstractmethod
    async def close(self) -> None: ...