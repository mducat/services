#!/bin/python

import aiohttp.web
import socketio

from conn import QueueClient


aio_app = aiohttp.web.Application()
sio = socketio.AsyncServer(cors_allowed_origins='*')

client = QueueClient()


class Namespace(socketio.AsyncNamespace):

    def __init__(self):
        super(Namespace, self).__init__(namespace='/ws')

    @staticmethod
    def process(data):
        return client.process(data)

    @staticmethod
    async def on_connect(*_):
        print(_)

    async def on_add_to_queue(self, sid, data):
        print('to', sid, flush=True)
        await sio.emit('processed', data={'data': self.process(data['data'])}, to=sid)


if __name__ == "__main__":
    n = Namespace()
    sio.register_namespace(n)
    sio.attach(aio_app)

    aiohttp.web.run_app(aio_app, port=8000)
    pass

