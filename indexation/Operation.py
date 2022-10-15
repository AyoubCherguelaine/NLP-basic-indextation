from curses import termname
import math
from pydoc import doc
from unicodedata import name
from indexation import (Query,Token)
from mongoConnector import db


class Operation:

    def __init__(self,query,method=0):
        self.method=method
        self.query = query
        self.db = db.db("""mongodb://ayoubchergue:Ayoub12456789@ac-kefvrhv-shard-00-00.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-01.wrubdwv.mongodb.net:27017,ac-kefvrhv-shard-00-02.wrubdwv.mongodb.net:27017/?ssl=true&replicaSet=atlas-she98u-shard-0&authSource=admin&retryWrites=true&w=majority""")
        self.DocsList=[]



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
    def compareInnerProductDist(Query,Document):
        score=0.0
        termMatch = 0
        for i in Query.TermFrequency :
            if i in Document['TermFrequency']:
                termMatch = termMatch +1
                prod = Query.TermFrequency[i] *Document['TermFrequency'][i]
                score=score + prod

        return (score ,termMatch)   


    @staticmethod
    def ConvertToDict(doc):
        tf={}
        print(doc['TermFrequency'])
        for i in doc['TermFrequency']:
            print(i)
            tf[i[0]]=i[1]
        return tf
   
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
    def compareDiceDict(Query,Document):
        score=0.0
        termMatch = 0
        prod=0.0
        p2=0.0
        p3=0.0
        for i in Query.TermFrequency :
            if i in Document['TermFrequency']:
                termMatch = termMatch +1
                prod = prod+ Query.TermFrequency[i] * Document['TermFrequency'][i]
                p2= p2 + Query.TermFrequency[i]**2
                p3= p3 + Document['TermFrequency'][i] **2

        score = (2*prod) / (p2 +p3 +0.0001) 
       
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
    def compareCosinusDict(Query,Document):
        score=0.0
        termMatch = 0
        prod=0.0
        p2=0.0
        p3=0.0
        for i in Query.TermFrequency :
            if i in Document['TermFrequency']:
                termMatch = termMatch +1
                prod = prod+ Query.TermFrequency[i] *Document['TermFrequency'][i] 
                p2= p2 + Query.TermFrequency[i]**2
                p3= p3 + Document['TermFrequency'][i] **2

        score = prod / math.sqrt( (p2*p3 +0.0001) )
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

    @staticmethod
    def compareJaccardDist(Query,Document):
        score=0.0
        termMatch = 0
        prod=0.0
        p2=0.0
        p3=0.0
        for i in Query.TermFrequency :
            if i in Document['TermFrequency']:
                termMatch = termMatch +1
                prod = prod+ Query.TermFrequency[i] *Document['TermFrequency'][i]
                p2= p2 + Query.TermFrequency[i]**2
                p3= p3 + Document['TermFrequency'][i] **2

        score = (prod) / (p2 +p3 - prod +0.0001) 
        return (score ,termMatch)   

    def  __GetDocs(self):
        idList=self.db.GetIds('documents')
        return idList

    def __getOneDoc(self,id):
        q = {'_id':id}
        doc = self.db.GetDocument('documents',q)  
        return doc

    def Operation(self):
        idList= self.__GetDocs()

        for i in idList:
            doc = self.__getOneDoc(i)
            #doc['TermFrequency']=  Operation.ConvertToDict(doc)
            l = []
            l.append(doc['name'])
            l.append(doc['path'])
            if self.method == 0:
                #with inner product
                score,termMatch = Operation.compareInnerProductDist(self.query,doc)
                l.append(score)
                l.append(termMatch)
            else :
                if self.method == 1 :
                    #with dice 
                    score,termMatch = Operation.compareDiceDict(self.query,doc)
                    l.append(score)
                    l.append(termMatch)
                else:
                    if self.method == 2 : 
                        score,termMatch = Operation.compareCosinusDict(self.query,doc)
                        l.append(score)
                        l.append(termMatch)
                    else: 
                        if self.method == 3:  
                            score,termMatch = Operation.compareJaccardDist(self.query,doc)
                            l.append(score)
                            l.append(termMatch)
            
            self.DocsList.append(l)
        d= self.DocsList
    
        d.sort( key= lambda d:d[2],reverse=True)
        self.DocsList =d
        return  d

    def preTestOperation(self):
        idList= self.__GetDocs()
        print(idList)

        for i in idList:
            doc = self.__getOneDoc(i)
            print(doc['name'])
            print(doc['path'])

    def GetDoc(self,name):
        return self.db.GetDocument('documents',{'name':name})
