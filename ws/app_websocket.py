import asyncio

import socketio
import aiohttp.web

from services.nats_process_service import ProcessService

flag = 0

if flag == 0:
    from services.nats_queue import QueueClient
elif flag == 1:
    from services.pika_queue import QueueClient


class Namespace(socketio.AsyncNamespace):

    def __init__(self):
        super(Namespace, self).__init__(namespace='/')

        self.client = QueueClient()
        asyncio.get_event_loop().create_task(ProcessService().init())
        asyncio.get_event_loop().create_task(self.client.init())

    @staticmethod
    async def on_connect(sid, *_):
        print(sid)

    async def on_add_to_queue(self, sid, data):
        processed = await self.client.process(data['data'])
        await sio.emit('processed', data={'data': processed}, to=sid, namespace='/')


if __name__ == "__main__":

    aio_app = aiohttp.web.Application()
    sio = socketio.AsyncServer(cors_allowed_origins='*')

    n = Namespace()
    sio.register_namespace(n)
    sio.attach(aio_app)

    aiohttp.web.run_app(aio_app, port=8000)
    pass

