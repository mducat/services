import asyncio
import nats.aio.client


class QueueClient:
    def __init__(self):
        self.nats = nats.aio.client.Client()
        self.loop = asyncio.get_event_loop()
        self._future_resp = asyncio.Future()

    def run(self):
        self.loop.create_task(self.init())
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass

    async def init(self):
        await self.nats.connect("demo.nats.io:4222", loop=asyncio.get_event_loop())
        await self.nats.subscribe("reverted", cb=self.identity)

    async def identity(self, msg):
        self._future_resp.set_result(msg.data.decode())

    async def process(self, data):
        await self.nats.publish("process", str.encode(data))

        resp = await self._future_resp
        self._future_resp = asyncio.Future()
        return resp
