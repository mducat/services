import socketio
import aiohttp.web


from services.nats_queue import QueueClient


class Namespace(socketio.AsyncNamespace):

    def __init__(self):
        super(Namespace, self).__init__(namespace='/')

        self.client = QueueClient()

    @staticmethod
    async def on_connect(sid, *_):
        print(sid)

    async def on_add_to_queue(self, sid, data):
        print("ICI", data['data'])
        processed = await self.client.process(data['data'])
        print("processed", processed)
        # processed = data
        await sio.emit('processed', data={'data': processed}, to=sid, namespace='/')


if __name__ == "__main__":

    aio_app = aiohttp.web.Application()
    sio = socketio.AsyncServer(cors_allowed_origins='*')

    n = Namespace()
    sio.register_namespace(n)
    sio.attach(aio_app)

    aiohttp.web.run_app(aio_app, port=8000)
    pass

