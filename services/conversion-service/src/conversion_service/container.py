
from infra.cache.implementation.redis import RedisCache
from infra.database.implementation.postgres import PostgresDatabase
from infra.messaging.schemas.bus_entities import BuildSchema, ExchangeType, QueueType
from infra.messaging.startup.bootstrap import MessageringBootstrap

from conversion_service.settings import ConversionServiceSettings

from conversion_service.application.use_case.create_conversion_job import CreateConversionJobUseCase
from conversion_service.application.use_case.get_conversion_job import GetConversionJobUseCase

from conversion_service.infrastructure.database.repositories.conversion import ConversionJobRepository
from conversion_service.infrastructure.database.repositories.user import UserRepository
from infra.storage.s3 import S3Storage

schema = BuildSchema(
    exchanges=[
        ExchangeType(
            exchange_name="exchange",
            exchange_type="direct",
            durable=True
        )
    ],
    queues=[
        QueueType(
            queue_name="account",
            exchange_name="exchange",
            bindings=[
                "account.request", 
                "account.response", 
                "account.created", 
                "account.updated", 
                "account.deleted"
                ],
            durable=True
        ),
    ])

class AppContainer():
    def __init__(self):
        self.settings = ConversionServiceSettings()

        self.msg_bootstrap = MessageringBootstrap(self.settings.MESSAGERING_ENV.url, schema)

        self.cache = RedisCache(
            self.settings.CACHE_ENV.host, 
            self.settings.CACHE_ENV.port
            )
        
        self.repo = PostgresDatabase(
            self.settings.DB_ENV.host, 
            self.settings.DB_ENV.port, 
            self.settings.DB_ENV.user, 
            self.settings.DB_ENV.password, 
            self.settings.DB_ENV.dbname
        )

        self.storage = S3Storage("my_bucket")
    
    def _build_repositories(self):
        self.conversion_repo = ConversionJobRepository(self.repo)
        self.user_repo = UserRepository(self.repo)


    def _build_use_cases(self):
        self.create_conversion_job_use_case = CreateConversionJobUseCase(
            self.conversion_repo, 
            self.user_repo, 
            self.cache, 
            self.bus, 
            self.storage
            )
        
        self.get_conversion_job_use_case = GetConversionJobUseCase(self.conversion_repo, self.cache, self.bus)


    async def startup(self):
        self.bus = await self.msg_bootstrap.start()
        await self.cache.build()
        await self.repo.connect()

        self._build_repositories()
        self._build_use_cases()

        return self

    
    async def shutdown(self):
        await self.repo.close()
        await self.msg_bootstrap.close()