#!/usr/bin/env python
# receive.py - receive messages from rabbitmq via pika
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('172.19.0.2'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
