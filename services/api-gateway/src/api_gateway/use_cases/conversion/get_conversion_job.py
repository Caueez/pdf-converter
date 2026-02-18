
import asyncio
from dataclasses import asdict
import hashlib
from typing import Any
import uuid



class GetConversionJobUseCase:
    def __init__(self, http_client : HTTPClient) -> None:
        self.http_client = http_client

    async def execute(self, job_id: str) -> dict[str, Any]:
        return {
            "job_id": job_id,
            "status": "pending"
            }
