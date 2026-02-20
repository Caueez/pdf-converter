
import asyncio
from dataclasses import asdict
import hashlib
from typing import Any
import uuid

<<<<<<< HEAD
from infra.http.interface.http import HttpInterface

class GetConversionJobUseCase:
    def __init__(self, http_client : HttpInterface) -> None:
        self.http_client = http_client

    async def execute(self, job_id: str) -> dict[str, Any]:
        try:
            response = await self.http_client.get(f"http://conversion-service:8000/conversion/{job_id}")
            return response
        except Exception as e:
            raise Exception(e)
=======


class GetConversionJobUseCase:
    def __init__(self, http_client : HTTPClient) -> None:
        self.http_client = http_client

    async def execute(self, job_id: str) -> dict[str, Any]:
        return {
            "job_id": job_id,
            "status": "pending"
            }
>>>>>>> 169784b (partial: api-gateway service implementation)
