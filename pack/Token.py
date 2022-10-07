#import nltk
#nltk.download('punkt')
#nltk.download('PorterStemmer')
#nltk.download('stopwords')
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

class token:

#    
# 
#     

    def __init__(self,file):
        self.path= './data/'+file
        f= open(self.path, 'r')
        self.content = f.read()

    def StopWord(self):
        #self.Tokens
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in self.Tokens if not w.lower() in stop_words]
        self.Tokens=filtered_sentence

    def steming(self):
        ps = PorterStemmer()
        
        stem = [ps.stem(w) for w in self.Tokens ]
        self.Tokens=stem
          

    def tokinize(self):
        self.Tokens= word_tokenize(self.content)
        
        self.StopWord()
        self.steming()
        self.RemovePunc()
      
        return self.Tokens
  
    def has_alphanum(self,token):
        return token.lower().islower() or any(character.isdigit() for character in token)

    def RemovePunc(self):
        
        res = [token for token in self.Tokens if self.has_alphanum(token)]
        self.Tokens=res