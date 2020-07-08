
import pymongo
from pymongo import MongoClient
import sys
from datetime import datetime


print("start")
#print("sys.prefix:", sys.prefix)

post = {
    "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    "temp": 21.7
}

client = pymongo.MongoClient("mongodb+srv://dbuser:bluebear@cluster01-enjmv.gcp.mongodb.net/temperatures?retryWrites=true&w=majority")

# for db in client.list_databases():
#     print(db)

with client:    
    db = client.temperatures
    records = db.office.find()
    for record in records:
        #print(record)
        print record['timestamp'].encode('utf8'),record['temp'] 

with client:    
    db = client.temperatures
    records = db.office.insert_one(post)

print ("--insert--")

with client:    
    db = client.temperatures
    records = db.office.find()
    for record in records:
        #print(record)
        print record['timestamp'].encode('utf8'),record['temp'] 
print("end")
