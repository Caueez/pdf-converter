
import asyncio
from dataclasses import asdict
import hashlib
from typing import Any
import uuid

<<<<<<< HEAD
from infra.http.interface.http import HttpInterface


class GetAccountUseCase:
    def __init__(self, http_client : HttpInterface) -> None:
        self.http_client = http_client

    async def execute(self, account_id: str) -> dict[str, Any]:
        try:
            response = await self.http_client.get(f"http://account-service:8000/account/{account_id}")
            return response
        except Exception as e:
            raise Exception(e)
=======



class GetAccountUseCase:
    def __init__(self, http_client : HTTPClient) -> None:
        self.http_client = http_client

    async def execute(self, id: str) -> dict[str, Any]:
        return {"id": id}
>>>>>>> 169784b (partial: api-gateway service implementation)
