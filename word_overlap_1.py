docs = [
    "ai is future",
    "dog is animal",
    "ml is part of ai"
]

query = "ai ml"

query_words = set(query.split())

best_doc = ""
max_count = 0

for doc in docs:
    count = 0
    for word in doc.split():
        if word in query_words:
            count += 1

    if count > max_count:
        max_count = count
        best_doc = doc

print(best_doc)