
import asyncio
from dataclasses import asdict
import hashlib
from typing import Any
import uuid

<<<<<<< HEAD
from infra.http.interface.http import HttpInterface



class CreateConversionJobUseCase:
    def __init__(self, http_client : HttpInterface) -> None:
        self.http_client = http_client

    async def execute(self, conversion_config: str) -> dict[str, Any]:
        try:
            response = await self.http_client.post("http://conversion-service:8000/conversion", data=conversion_config)
            return response
        except Exception as e:
            raise Exception(e)

        
        
            # return {
            #     "conversion_config": conversion_config,
            #     "job_id": str(uuid.uuid4()),
            #     "status": "pending",
            #     "message": "Conversion job created",
            #     "presigned_url": "https://example.com/presigned_url"
            #     }
=======


class CreateConversionJobUseCase:
    def __init__(self, http_client : HTTPClient) -> None:
        self.http_client = http_client

    async def execute(self, conversion_config: str) -> dict[str, Any]:
        return {
            "conversion_config": conversion_config,
            "job_id": str(uuid.uuid4()),
            "status": "pending",
            "message": "Conversion job created",
            "presigned_url": "https://example.com/presigned_url"
            }
>>>>>>> 169784b (partial: api-gateway service implementation)
