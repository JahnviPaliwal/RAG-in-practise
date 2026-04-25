text = "ai ml ai data ml ai engineering python python"

frq = {}

for i in text.split():
    frq[i] = frq.get(i,0)+1

max_frq = 0
max_word = ""

for words, count in frq.items():
    if count>max_frq:
        max_frq = count
        max_word = words

print(max_word, max_frq)

