import asyncio
import nats.aio.client


class ProcessService:
    def __init__(self):
        self.nats = nats.aio.client.Client()

    async def init(self):
        await self.nats.connect("demo.nats.io:4222", loop=asyncio.get_event_loop())
        return self

    async def process(self, msg):
        print("1", msg)
        reverted = str.encode(msg.data.decode()[::-1])
        print("reverted", reverted)
        await self.nats.connect("demo.nats.io:4222", loop=asyncio.get_event_loop())
        await self.nats.publish(msg.reply, reverted)
