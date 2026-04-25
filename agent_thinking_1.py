query = "add 10 and 20"

emb  = {"add":"calculator"}
result = "search"
for i in query.split():
    if i in emb:
        result = emb[i]

print(result)