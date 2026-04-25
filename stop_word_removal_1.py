docs = [
    "ai is the future",
    "ml is part of ai",
    "the dog is animal"
]

query = "what is the ai"

stopwords = {"is", "the", "what"}
new_q = []
total_count = []

for i in query.split():
    if i not in stopwords:
        new_q.append(i)
print("New ququq:",new_q )

for lines in docs:
    count = 0
    for words in lines.split():
        if words in new_q:
            count+=1
    total_count.append(count)

print(total_count)
print(docs[total_count.index(max(total_count))])
# print(docs[docs.index())])