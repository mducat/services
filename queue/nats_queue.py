#!/bin/python

import pika
import uuid
import nats.aio.client


class QueueClient:
    def __init__(self):
        self.nats = nats.aio.client.Client()

    def process(self, data):
        destination = ''
        self.nats.publish(destination, data)

