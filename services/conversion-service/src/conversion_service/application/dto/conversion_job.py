
from dataclasses import dataclass


@dataclass
class ConversionJobDto:
    user_id: str
    job_id: str
    status: str
    bucket_name: str
    storage_key: str