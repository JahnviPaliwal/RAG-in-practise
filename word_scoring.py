docs = [
    "ai is future data",
    "dog animal data",
    "ml ai systems data"
]

weights = {
    "ai": 3,
    "ml": 2,
    "data": 1
}

scores = []

for doc in docs:
    count = 0
    for word in doc.split():
        if word in weights:
            count += weights[word]

    scores.append(count)

print(scores)
max_index = scores.index(max(scores))

print(docs[max_index])