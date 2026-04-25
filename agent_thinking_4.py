docs = [
    "ai is future",
    "ml is part of ai",
    "dogs are animals"
]

query = "what is ai and add 10 20"

# tool detection
tools = {
    "add": "calculator",
    "sum": "calculator",
    "subtract": "calculator"
}

result = []

# check calculator (word-level)
for word in query.split():
    if word in tools and "calculator" not in result:
        result.append("calculator")

# check search intent (phrase-level)
if "what is" in query:
    result.append("search")

# --- RAG PART ---
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

# --- OUTPUT ---
for tool in result:
    print(tool)

if "search" in result:
    print("best doc:", best_doc)