from abc import ABC, abstractmethod

from conversion_service.domain.entitities.conversion_job import ConversionJob


class ConversionJobRepositoryInterface(ABC):
    @abstractmethod
    async def create_conversion_job(self, conversion_job: ConversionJob) -> None:
        pass

    @abstractmethod
    async def get_conversion_job(self, job_id: str) -> ConversionJob:
        pass