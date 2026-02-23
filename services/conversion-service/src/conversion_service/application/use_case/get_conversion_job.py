
from infra.cache.interface.cache import CacheInterface
from infra.messaging.interface.bus import BusInterface

from conversion_service.application.ports.repositories.conversion_job import ConversionJobRepositoryInterface

from conversion_service.application.mappers.conversion_job import MapperConversionJob

from conversion_service.application.dto.conversion_job import ConversionJobDto


class GetConversionJobUseCase:
    def __init__(
            self, 
            conversion_repo : ConversionJobRepositoryInterface, 
            cache : CacheInterface, 
            bus : BusInterface):
        self.conversion_repo = conversion_repo
        self.cache = cache
        self.bus = bus
    
    async def execute(self, dto: ConversionJobDto):

        conversion_job = await self.conversion_repo.get_conversion_job(dto.job_id)

        if not conversion_job:
            raise Exception("Conversion job not found")
        
        return MapperConversionJob.to_api(conversion_job)