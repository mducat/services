import asyncio


class ProcessService:
    def __init__(self):
        import nats.aio.client
        self.nats = nats.aio.client.Client()

    async def init(self):
        await self.nats.connect("demo.nats.io:4222", loop=asyncio.get_event_loop())
        return self

    async def process(self, msg):
        print("1", msg)
        await self.nats.connect("demo.nats.io:4222", loop=asyncio.get_event_loop())
        await self.nats.publish(msg.subject, msg.data[::-1])
