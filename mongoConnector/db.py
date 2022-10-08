
import pymongo

class db :
    def __init__(self ,keyInit=0):
        
        client = pymongo.MongoClient(keyInit)
        db = client.test
        
        
        self.db = client.gettingStarted
        print('Atlas mongo connected')
        
        
        
    
    def CreateCollection(self,name):
        col = self.db.create_collection(name)
        
        return col

    def GetCollection(self,ColName):
        
        return self.db.get_collection(ColName)
        
        
        
        
                


    def AddDocument(self,ColName,obj):
        
        col = self.db.get_collection(ColName)
        
        r =col.insert_one(obj) 
        return r
        

    def GetDocument(self,ColName,search):
        #search is a dict : { "name.last": "Turing" }
        
        
        col = self.db.get_collection(ColName)
        doc = col.find_one(search)

        return doc

    def GetDocs(self,ColName,query={}):
        col=self.db.get_collection(ColName)    
        d = col.find(query)
        
        return d    


    def CountDoc(self,ColName,query={}):
        col=self.db.get_collection(ColName)    
        v = col.count_documents(query)
        return v


    def DeleteOne(self,ColName,query={}):
        #{ "_id" : ObjectId("563237a41a4d68582c2509da") }
        try:
            col = self.db.get_collection(ColName)
            col.orders.deleteOne( query )
        except:
            print('Err')

         

                

