from indexation import (Query,Token)
from mongoConnector import db


class Operation:

    def __init__(self,query):
        self.query = query
        self.db = db.db("""mongodb://ayoubchergue:Ayoub12456789@ac-kefvrhv-shard-00-00.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-01.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-02.wrubdwv.mongodb.net:27017/?ssl=true&replicaSet=atlas-she98u-shard-0&authSource=admin&retryWrites=true&w=majority""")

    def GetDocs(self):
        return [22,22]

    @staticmethod
    def compare(Query,Document):
        score=0.0
        for i in Query,TermFrequency :
            if i in list(Document.TermFrequency.keys()):
                
                score=1.0

        return score    



