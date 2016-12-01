#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='172.19.0.2'))
channel = connection.channel()

channel.echange_declare(exchange='logs',
                        type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [x] Sent %r" %message)

connection.close()