from enum import Enum


class JobStatus(Enum):
    CREATED = "created"
    WAITING_UPLOAD = "waiting_upload"
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"