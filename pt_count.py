text = "ai engineer ai ml ai data"

feq = {}


for i in text:
    feq[i] = feq.get(i,0)+1

print(feq)
maxi = 0
max_w =""
for word, i in feq.items():
    if i>maxi:
        maxi = i
        max_w = word

print(max_w)
