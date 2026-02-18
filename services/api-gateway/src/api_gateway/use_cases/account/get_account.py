
import asyncio
from dataclasses import asdict
import hashlib
from typing import Any
import uuid




class GetAccountUseCase:
    def __init__(self, http_client : HTTPClient) -> None:
        self.http_client = http_client

    async def execute(self, id: str) -> dict[str, Any]:
        return {"id": id}
