text = "ai ml ai data ml engineering python"

frq = {}

for i in text.split():
    frq[i] = frq.get(i,0)+1

words = []
for word, i in frq.items():
    if i == 1:
        words.append(word)

for i in words:
    print(i)
