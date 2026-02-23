
from typing import Any

from conversion_service.application.dto.conversion_job import ConversionJobDto

from conversion_service.domain.entitities.conversion_job import ConversionJob


class MapperConversionJob:
    @staticmethod
    def to_api(entity: ConversionJob) -> ConversionJobDto:
        return ConversionJobDto(
            user_id=entity.user_id,
            job_id = entity.job_id,
            status = entity.status.name,
            bucket_name=entity.bucket_name,
            storage_key=entity.bucket_name
        )