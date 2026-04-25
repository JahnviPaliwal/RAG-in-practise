docs = [
    "ai ml data",
    "ai data",
    "ml systems"
]

query = "ai ml"

# Step 1: doc frequency
doc_count = {}

for doc in docs:
    words = set(doc.split())
    for word in words:
        doc_count[word] = doc_count.get(word, 0) + 1

# Step 2: weights
weights = {}
for word, count in doc_count.items():
    weights[word] = 1 / count

# Step 3: scoring
query_words = set(query.split())

best_doc = ""
max_score = 0

for doc in docs:
    score = 0
    for word in doc.split():
        if word in query_words:
            score += weights[word]

    if score > max_score:
        max_score = score
        best_doc = doc

print(best_doc)