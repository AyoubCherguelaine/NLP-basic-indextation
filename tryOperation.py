from webbrowser import Opera
from indexation import (Query,Token,Operation)

# import and preprocess file.txt
t = Token.token('file.txt')

# test tokenization doxument


# preprocess query

q= Query.query("""In this tutorial, you will learn what a categorical variable is, along with three approaches for handling this type of data.

""")

# test tokenization Query



# get operation
print("\n inner")

score,termMatch = Operation.Operation.compareInnerProduct(q,t)

print(score)


print(termMatch)

print("\n Dice")

score,termMatch = Operation.Operation.compareDice(q,t)

print(score)


print(termMatch)

print("\n Cos")
score,termMatch = Operation.Operation.compareCosinus(q,t)

print(score)


print(termMatch)

print("\n Jaccard")
score,termMatch = Operation.Operation.compareJaccard(q,t)

print(score)


print(termMatch)
