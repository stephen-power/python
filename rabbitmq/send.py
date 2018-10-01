#!/usr/bin/python
import pika

print("start")
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='fred bear woz ere')
print(" [x] Sent 'fred bear woz ere!'")
connection.close()


print("end")
