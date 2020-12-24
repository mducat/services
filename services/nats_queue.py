import asyncio

from services.nats_process_service import ProcessService


class QueueClient:
    def __init__(self):
        self.process_service = ProcessService()
        import nats.aio.client
        self.nats = nats.aio.client.Client()

    async def subscribe(self):
        await self.nats.subscribe("process", cb=self.process_service.process)

    async def init(self):
        await self.nats.connect("demo.nats.io:4222", loop=asyncio.get_event_loop())
        # self.process_service = self.process_service.init()
        await self.subscribe()
        return self

    async def process(self, data):
        await self.init()

        # await self.nats.publish("process", str.encode(data))

        response = None
        while not response:
            response = await self.nats.request("process", str.encode(data))

        return response