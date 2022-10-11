from mongoConnector import db
from indexation import Token

tk = Token.token('Approache.txt')
doc = tk.Obj()

db = db.db("mongodb://ayoubchergue:Ayoub12456789@ac-kefvrhv-shard-00-00.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-01.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-02.wrubdwv.mongodb.net:27017/?ssl=true&replicaSet=atlas-she98u-shard-0&authSource=admin&retryWrites=true&w=majority")


#db.AddDocument('documents',doc)


def new_func():
    col = db.GetCollection('documents')
    return col

col = new_func()

print(col.distinct('path'))