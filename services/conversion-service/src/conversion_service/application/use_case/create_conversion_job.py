

from infra.cache.interface.cache import CacheInterface
from infra.messaging.interface.bus import BusInterface

from conversion_service.application.ports.repositories.conversion_job import ConversionJobRepositoryInterface
from conversion_service.application.ports.repositories.user import UserRepositoryInterface

from conversion_service.application.ports.storage import StorageInterface

from conversion_service.domain.entitities.conversion_job import ConversionJob

from conversion_service.application.dto.conversion_job import ConversionJobDto
from conversion_service.application.mappers.conversion_job import MapperConversionJob


class CreateConversionJobUseCase:
    def __init__(
            self, 
            conversion_repo : ConversionJobRepositoryInterface, 
            user_repo: UserRepositoryInterface, 
            cache : CacheInterface, 
            bus : BusInterface, 
            storage: StorageInterface
            ):
        self.conversion_repo = conversion_repo
        self.user_repo = user_repo
        self.cache = cache
        self.bus = bus
        self.storage = storage
        
    
    async def execute(self, dto: ConversionJobDto):
        user_history = await self.user_repo.get_user_conversion_history(dto.user_id)
        user_history.can_upload()

        conversion_job = ConversionJob.create(dto.user_id)
        await self.conversion_repo.create_conversion_job(conversion_job)

        presigned_url = await self.storage.generate_presigned_url(conversion_job.bucket_name)

        conversion_job.wait_for_upload()
        
        # await self.bus.publish()

        user_history.add_active_job()

        await self.user_repo.upload_user_conversion_history(dto.user_id, user_history)

        return MapperConversionJob.to_api(conversion_job) # TODO: criar dto melhor