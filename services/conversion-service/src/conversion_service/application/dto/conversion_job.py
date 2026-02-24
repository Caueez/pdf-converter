
from dataclasses import dataclass
from typing import Optional


@dataclass
class ConversionJobDto:
    user_id: str
    job_id: Optional[str]
    status: Optional[str]
    presigned_url: Optional[str]