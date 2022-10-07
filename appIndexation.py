
from indexation import (Token,Sementic)

Token = Token.token('doc1.txt')

WordList= Token.tokinize()


index= Token.indexation()
print(index)

tf = Token.TermFrequencyCalc()
print('-------------------------------------------------------------')
print(tf)

print(max(tf))


