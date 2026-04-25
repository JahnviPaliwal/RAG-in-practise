docs = [
    "ai ml data science",
    "ai data engineering",
    "ml systems design",
    "data pipelines"
]

query = "ai ml data"

doc_count = {}

for doc in docs:
    words = set(doc.split())
    for word in words:
        doc_count[word] = doc_count.get(word,0)+1

weigths = {}

for word, count in doc_count.items():
    weigths[word] = 1/count

print(weigths)

query_spl = set(query.split())

total_score = []


for lines in docs:
    score = 0
    for word in lines.split():
        if word in query_spl:
            score+=weigths[word]

    total_score.append(score)


total_score.sort(reverse=True)
print(total_score)
# print(docs[total_score.index(max(total_score))])


#
# for doc in docs:
#     score = 0
#     for word in doc.split():
#         if word in query_words:
#             score += weights[word]
#
#     doc_scores.append((doc, score))
#
# # Step 4: sort by score
# doc_scores.sort(key=lambda x: x[1], reverse=True)
#
# # top 2
# for doc, score in doc_scores[:2]:
#     print(doc)