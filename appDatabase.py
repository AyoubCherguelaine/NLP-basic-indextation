

from mongoConnector import db
from indexation import Token
import pymongo


Token= Token.token('test.txt')

doc = Token.Obj()

print(doc)
client = pymongo.MongoClient("mongodb://ayoubchergue:Ayoub12456789@ac-kefvrhv-shard-00-00.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-01.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-02.wrubdwv.mongodb.net:27017/?ssl=true&replicaSet=atlas-she98u-shard-0&authSource=admin&retryWrites=true&w=majority")

        
        
db = client.gettingStarted
docs = db.get_collection('documents')
print("get docs")
doc1 = docs.find_one({'name':'doc1'})
result = docs.insert_one(doc)

print(doc1)
print(result)
