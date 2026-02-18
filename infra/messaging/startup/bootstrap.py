


from infra.messaging.startup.builder import MessageringBuilder
from infra.messaging.interface.bus import BusInterface
from infra.messaging.implementation.bus import RabbitBus
from infra.messaging.schemas.bus_entities import BuildSchema


class MessageringBootstrap:
    def __init__(self, url: str, schema: BuildSchema) -> None:
        self._url = url
        self._schema = schema
        self._messagering : RabbitBus | None = None
    
    async def close(self) -> None:
        await self._messagering.close()

    async def start(self) -> BusInterface:
        self._messagering = RabbitBus(self._url)
        builder = MessageringBuilder(self._schema, self._messagering)

        await builder.build()

        return self._messagering
