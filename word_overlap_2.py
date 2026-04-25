docs = [
    "ai ml data",
    "ai is future",
    "dog animal data",
    "ml ai systems"
]

query = "ai ml"
scored_docs = []

query_words = set(query.split())

for lines in docs:
    count = 0
    for word in lines.split():
        if  word in query_words:
            count+=1

    scored_docs.append((lines,count))

scored_docs.sort(key=lambda x: x[1], reverse = True)

top_2 = scored_docs[:2]

for doc, score in top_2:
    print(doc)

