
from indexation import (Query,Operation)

query = input("query : ")

q= Query.query(query)

o = Operation.Operation(q,method=2)

d = o.GetDoc('file')


l =o.Operation()

print(l)