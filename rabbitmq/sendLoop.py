#!/usr/bin/python
import pika
from datetime import datetime

print("start")
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
tstart = datetime.now()
for i in range(1,10000000):
    channel.basic_publish(exchange='',routing_key='hello',body= str(i) + '  fred bear woz ere')
    #print( str(i) + " Sent 'fred bear woz ere!'")
tend = datetime.now()
connection.close()


print( str(i) + " messages put.  time="  + str(tend - tstart))
