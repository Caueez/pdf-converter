
import asyncio
from dataclasses import asdict

from api_gateway.settings import ApiGatewaySettings

from infra.cache import RedisCache

from infra.database import PostgresDatabase

from infra.messaging import MessageringBootstrap
from infra.messaging.schemas.bus_entities import BuildSchema, ExchangeType, QueueType

from api_gateway.use_cases.account import CreateAccountUseCase, GetAccountUseCase
from api_gateway.use_cases.conversion import CreateConversionJobUseCase, GetConversionJobUseCase


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


class AppContainer:
    def __init__(self) -> None:
        self.settings = ApiGatewaySettings()

        self.msg_bootstrap = MessageringBootstrap(self.settings.MESSAGERING_ENV.url, schema)

        self.http_client = HTTPClient()

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

        self.create_account_use_case = CreateAccountUseCase(self.http_client)
        self.get_account_use_case = GetAccountUseCase(self.http_client)

        self.create_conversion_job_use_case = CreateConversionJobUseCase(self.http_client)
        self.get_conversion_job_use_case = GetConversionJobUseCase(self.http_client)

    async def startup(self):
        self.bus = await self.msg_bootstrap.start()
        await self.cache.build()
        await self.repo.connect()

        return self

    async def shutdown(self):
        await self.repo.close()
        await self.msg_bootstrap.close()
