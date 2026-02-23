
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from uuid import uuid4

from conversion_service.domain.value_objects.job_status import JobStatus


# TODO: add url validation class

@dataclass
class ConversionJob:
    user_id: str
    job_id: str
    _status: JobStatus
    bucket_name: Optional[str]
    storage_key: Optional[str]

    @classmethod
    def create(cls, user_id: str):        
        return cls(
            user_id = user_id,
            job_id = str(uuid4()),
            _status = JobStatus.CREATED,
            bucket_name = None,
            storage_key = None
        )
    
    @property
    def status(self):
        return self._status

    def wait_for_upload(self):
        if self._status != JobStatus.CREATED:
            raise Exception("Job is not in created state")
        self._status = JobStatus.WAITING_UPLOAD
    
    def enter_process_queue(self):
        if self._status != JobStatus.WAITING_UPLOAD:
            raise Exception("Job is not in waiting upload state")
        self._status = JobStatus.PENDING

    def start_processing(self):
        if self._status != JobStatus.PENDING:
            raise Exception("Job is not in pending state")
        self._status = JobStatus.PROCESSING

    def complete(self):
        if self._status != JobStatus.PROCESSING:
            raise Exception("Job is not in processing state")
        self._status = JobStatus.COMPLETED
