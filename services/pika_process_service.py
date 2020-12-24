#!/bin/python

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='queue')


def simple_process(data):
    data
    return data[::-1]


def handle(ch, method, props, body):
    print("Queue service recieved '%s'" % body)
    response = simple_process(body.decode("utf-8"))

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='queue', on_message_callback=handle)

print("Queue service started !")
channel.start_consuming()

