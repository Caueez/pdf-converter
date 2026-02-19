


from infra.cache.interface.cache import CacheInterface
from infra.database.implementation.repository import DatabaseRepository
from infra.messaging.interface.bus import BusInterface

from conversion_service.schemas.conversion import DefaultPayload

class GetConversionJobUseCase:
    def __init__(
            self, 
            repo : DatabaseRepository, 
            cache : CacheInterface, 
            bus : BusInterface):
        self.repo = repo
        self.cache = cache
        self.bus = bus
    
    async def execute(self, payload: DefaultPayload):
        ...