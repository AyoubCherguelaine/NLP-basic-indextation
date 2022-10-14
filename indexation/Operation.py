from curses import termname
import math
from indexation import (Query,Token)
from mongoConnector import db


class Operation:

    def __init__(self,query):
        self.query = query
        self.db = db.db("""mongodb://ayoubchergue:Ayoub12456789@ac-kefvrhv-shard-00-00.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-01.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-02.wrubdwv.mongodb.net:27017/?ssl=true&replicaSet=atlas-she98u-shard-0&authSource=admin&retryWrites=true&w=majority""")

    def GetDocs(self):
        return [22,22]

    # this methode is tested // alger
    @staticmethod
    def compareInnerProduct(Query,Document):
        score=0.0
        termMatch = 0
        for i in Query.TermFrequency :
            if i in Document.TermFrequency:
                termMatch = termMatch +1
                prod = Query.TermFrequency[i] *Document.TermFrequency[i] 
                score=score + prod

        return (score ,termMatch)   

    @staticmethod
    def compareToken(Query,Document):
        score=0.0
        termMatch = 0
        for i in Query.index :
            if i in Document.index:
                
                termMatch = termMatch +1

                prod = Query.index[i] /Document.index[i] 
                score=score + prod
        matching = score/termMatch
        return (score ,termMatch,matching)   


    @staticmethod
    def compareDice(Query,Document):
        score=0.0
        termMatch = 0
        prod=0.0
        p2=0.0
        p3=0.0
        for i in Query.TermFrequency :
            if i in Document.TermFrequency:
                termMatch = termMatch +1
                prod = prod+ Query.TermFrequency[i] *Document.TermFrequency[i] 
                p2= p2 + Query.TermFrequency[i]**2
                p3= p3 + Document.TermFrequency[i] **2

        score = (2*prod) / (p2 +p3) 
        return (score ,termMatch)   

    @staticmethod
    def compareCosinus(Query,Document):
        score=0.0
        termMatch = 0
        prod=0.0
        p2=0.0
        p3=0.0
        for i in Query.TermFrequency :
            if i in Document.TermFrequency:
                termMatch = termMatch +1
                prod = prod+ Query.TermFrequency[i] *Document.TermFrequency[i] 
                p2= p2 + Query.TermFrequency[i]**2
                p3= p3 + Document.TermFrequency[i] **2

        score = prod / math.sqrt( (p2*p3) )
        return (score ,termMatch)   




    @staticmethod
    def compareJaccard(Query,Document):
        score=0.0
        termMatch = 0
        prod=0.0
        p2=0.0
        p3=0.0
        for i in Query.TermFrequency :
            if i in Document.TermFrequency:
                termMatch = termMatch +1
                prod = prod+ Query.TermFrequency[i] *Document.TermFrequency[i] 
                p2= p2 + Query.TermFrequency[i]**2
                p3= p3 + Document.TermFrequency[i] **2

        score = (prod) / (p2 +p3 - prod) 
        return (score ,termMatch)   

