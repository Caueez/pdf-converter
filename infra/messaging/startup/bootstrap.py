


from infra.messaging.startup.builder import MessageringBuilder
from infra.messaging.interface.bus import BusInterface
from infra.messaging.implementation.bus import RabbitBus
from infra.messaging.schemas.bus_entities import BuildSchema

# TODO: Add settings interface type

class MessageringBootstrap:
    def __init__(self, settings, schema: BuildSchema) -> None:
        self._settings = settings
        self._schema = schema
        self._messagering : RabbitBus | None = None
    
    async def close(self) -> None:
        await self._messagering.close()

    async def start(self) -> BusInterface:
        self._messagering = RabbitBus(
            user=self._settings.MESSAGERING_ENV.user,
            password=self._settings.MESSAGERING_ENV.password,
            host=self._settings.MESSAGERING_ENV.host,
            port=self._settings.MESSAGERING_ENV.port
        )
        builder = MessageringBuilder(self._schema, self._messagering)

        await builder.build()

        return self._messagering
