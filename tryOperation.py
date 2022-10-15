
from indexation import (Query,Token,Operation)

# import and preprocess file.txt
d = Token.token('file.txt')

# test tokenization doxument

# preprocess query

q= Query.query("""Consider a survey that asks how often you """)




score,termMatch = Operation.Operation.compareDice(q,d)


# print("\n Dice")

# score,termMatch = Operation.Operation.compareDice(q,t)

print(score)


print(termMatch)


o = Operation.Operation(d,method=1)

d = o.GetDoc('file')


l =o.Operation()

print(l)