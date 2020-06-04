#!/bin/python

import pika
import uuid

class QueueClient():

    def __init__(self):
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        
        self.channel = self.conn.channel()
        
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback = result.method.queue
        
        self.channel.basic_consume(
            queue=self.callback,
            on_message_callback=self.handle,
            auto_ack=True)
        
    def handle(self, ch, method, props, body):
        if self.correlation == props.correlation_id:
            self.response = body
        pass

    def process(self, data):
        self.response = None
        self.correlation = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='queue',
            properties=pika.BasicProperties(
                reply_to=self.callback,
                correlation_id=self.correlation,
            ),
            body=str(data))
        while self.response is None:
            self.conn.process_data_events()
        return str(self.response.decode("utf-8"))
