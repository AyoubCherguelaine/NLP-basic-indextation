
from pymongo import MongoClient

class db :
    def __init__(self ,keyInit=0):
        v="DvWKB-9AYwpt4Vt"
        key=""
        if keyInit !=0:
            key=keyInit
        else:
            path= 'mongoConnector/Pass.txt'
            f= open(path, 'r')
            key = f.read()
            f.close()


        client = MongoClient(key)
        
        
        self.db = client.gettingStarted
        print('Atlas mongo connected')
        
        
        
    
    def CreateCollection(self,name):
        col = self.db.create_collection(name)
        self.Collections.append(col)
        return name

    def GetCollections(self):
        
        self.Collections= self.db.list_collection_names()
        return self.Collections
        
        
        
        
                


    def AddDocument(self,ColName,obj):
        
        col = self.db.get_collection(ColName)
        
        r =col.insert_one(obj) 
        return r
        

    def GetDocument(self,ColName,search):
        #search is a dict : { "name.last": "Turing" }
        
        
        col = self.db.get_collection(ColName)
        doc = col.find_one(search)

        return doc


