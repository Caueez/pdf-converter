

from infra.cache.interface.cache import CacheInterface
from infra.database.implementation.repository import DatabaseRepository
from infra.messaging.interface.bus import BusInterface

from conversion_service.repository.conversion import ConversionRepository

from conversion_service.schemas.conversion import DefaultPayload # TODO: Change to infra/schemas


class CreateConversionJobUseCase:
    def __init__(
            self, 
            repo : ConversionRepository, 
            cache : CacheInterface, 
            bus : BusInterface):
        self.repo = repo
        self.cache = cache
        self.bus = bus
        
    
    async def execute(self, payload: DefaultPayload):
        await self.repo.create_conversion_job(payload.job_id, payload.status, payload.message, payload.raw_presigned_url, payload.processed_presigned_url)
        await self.bus.publish()