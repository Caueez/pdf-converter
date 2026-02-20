
from dataclasses import dataclass

@dataclass
class ConversionJob:
    job_id: str
    status: str
    message: str
    presigned_url: str