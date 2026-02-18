
from httpx import AsyncClient

from infra.http.interface.http import HttpInterface


class HttpxClient(HttpInterface):
    def __init__(self):
        self.client = AsyncClient()

    async def get(self, url: str) -> dict:
        response = await self.client.get(url)
        return response.json()

    async def post(self, url: str, data: dict) -> dict:
        response = await self.client.post(url, json=data)
        return response.json()
    
    async def put(self, url: str, data: dict) -> dict:
        response = await self.client.put(url, json=data)
        return response.json()
     
    async def close(self):
        await self.client.aclose()
        self.client = None
    