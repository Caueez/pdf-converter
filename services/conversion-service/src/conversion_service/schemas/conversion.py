
from typing import Optional

from pydantic import BaseModel


class DefaultPayload(BaseModel):
    job_id: Optional[str]
    status: Optional[str]
    message: Optional[str]
    presigned_url: Optional[str]

class APIGatewayRequest(BaseModel):
    action: str
    timestamp: str
    payload: DefaultPayload
    