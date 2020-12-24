import asyncio
import nats.aio.client


class ProcessService:
    def __init__(self):
        self.nats = nats.aio.client.Client()
        self.loop = asyncio.get_event_loop()

    def run(self):
        """
        Launch init and prevents shutdown
        """
        self.loop.create_task(self.init())
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass

    async def init(self):
        """
        Connects to NATS and add metis modules in factory.
        """

        await self.nats.connect("demo.nats.io:4222", loop=asyncio.get_event_loop())
        await self.nats.subscribe('process', cb=self.revert)

    async def revert(self, msg):
        reverted = str.encode(msg.data.decode()[::-1])
        await self.nats.publish('reverted', reverted)
