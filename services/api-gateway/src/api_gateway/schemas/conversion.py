from pydantic import BaseModel

from typing import Optional


class CreateConversionJobRequest(BaseModel):
    conversion_config: Optional[str] # Only for testing

class GetConversionJobRequest(BaseModel):
    job_id: Optional[str] # Only for testing