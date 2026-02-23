
from typing import Any

from conversion_service.domain.entitities.conversion_job import ConversionJob, JobStatus


class MapperConversionJob:
    @staticmethod
    def to_domain(row) -> ConversionJob:
        status = JobStatus(row["status"])

        return ConversionJob(
            user_id = row["user_id"],
            job_id = row["job_id"],
            status = status,
            bucket_name=row["bucket_name"],
            storage_key=row["storage_key"]
        )