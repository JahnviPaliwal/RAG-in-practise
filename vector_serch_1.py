docs = [
    "ai ml",
    "data science",
    "dog animal",
    "ai data"
]

query = "ai"

embeddings = {
    "ai": [1, 1],
    "ml": [1, 1],
    "data": [0, 1],
    "science": [0, 1],
    "dog": [1, 0],
    "animal": [1, 0]
}
values = []
def sum_vc(list1):
    list2= []
    for i in list1[0]:
        for j in list1[1]:
            if i.index()== j.index():
                c = i+j
                list2.append(c)
    print(list2)
    return list2





for lines in docs:
    values = []
    for word in lines.split():
        values.append(embeddings[word])

    print(values)
    vectors = sum_vc(values)

    print(f"{word}-one line over\n")


# print(values)

