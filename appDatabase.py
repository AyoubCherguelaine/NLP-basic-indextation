
from mongoConnector import db
from indexation import Token


Token= Token.token('test.txt')

doc = Token.Obj()

print(doc)
db = db.db()
result = db.AddDocument('documents',doc)

print(result)
