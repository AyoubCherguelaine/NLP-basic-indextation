#import nltk
#nltk.download('punkt')
#nltk.download('PorterStemmer')
#nltk.download('stopwords')
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string



class token:


    def __init__(self,file):
        self.name= file.split(".")[0]
        self.path= './data/'+file
        f= open(self.path, 'r')
        self.content = f.read()
        f.close()
        self.__tokinize()
        self.__indexation()
        self.__TermFrequencyCalc()

    def __StopWord(self):
        #self.Tokens
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in self.Tokens if not w.lower() in stop_words]
        self.Tokens=filtered_sentence

    def __steming(self):
        ps = PorterStemmer()
        
        stem = [ps.stem(w) for w in self.Tokens ]
        self.Tokens=stem
          

    def __tokinize(self):
        self.Tokens= word_tokenize(self.content)
        
        self.__StopWord()
        self.__steming()
        self.__RemovePunc()
      
        return self.Tokens
  
    def __has_alphanum(self,token):
        return token.lower().islower() or any(character.isdigit() for character in token)

    def __RemovePunc(self):
        
        res = [token for token in self.Tokens if self.__has_alphanum(token)]
        self.Tokens=res

    def __indexation(self):
        WordList = self.Tokens
        self.index={}
        for w in WordList:
            if w =='***1':
                continue
            l = WordList.count(w)
            p= [w,l]
            self.index[w]=l
            
            while not (WordList.count(w) == 0):
                WordList[WordList.index(w) ]='***1'
        return self.index        

    def __TermFrequencyCalc(self):
        self.TermFrequency={}
        length = len(self.Tokens)
        
        for l in self.index:
            
            self.TermFrequency[l]= (self.index[l]/length)

            
            
        return self.TermFrequency    

    def Obj(self):
        doc ={
            'name':self.name,
            'path':self.path,
            'TermFrequency':self.TermFrequency
            }  

        return doc           