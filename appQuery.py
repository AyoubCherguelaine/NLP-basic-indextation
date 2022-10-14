from indexation import Query

# q=Query.query('hello evryone i m ayoub cherguelaine , i live in blida , im so talented , i have a lot of skills , if you want to contact me >> paypal.me')
# print(q.Tokens)
# q.indexation()

# print(q.index)

# q.TermFrequencyCalc()

# print(q.TermFrequency)
#print(q.Obj())

c = {
    'name':'ayoub',
    'age':44
}
d = {
    'name':'ayoub',
    'age':44,
    'profession':'rich'
}

for i in c:
    if i in list(d.keys()):
        print(i)