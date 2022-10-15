

from mongoConnector import db
from indexation import Token

from os import walk

db= db.db("""mongodb://ayoubchergue:Ayoub12456789@ac-kefvrhv-shard-00-00.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-01.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-02.wrubdwv.mongodb.net:27017/?ssl=true&replicaSet=atlas-she98u-shard-0&authSource=admin&retryWrites=true&w=majority""")


f=[]
for (dirpath, dirnames, filenames) in walk('./data'):
    
    f.extend(filenames)
    break

print(f)

for i in f : 
    t= Token.token(i)
    di=t.Obj()
    db.AddDocument('documents',di)

