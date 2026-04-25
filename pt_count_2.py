text = "ai ml ai data ml ai engineering"
feq = {}
for i in text.split():
    feq[i] = feq.get(i,0)+1


sortted = sorted(feq.items(), key=lambda x: x[1], reverse=True)

one = sortted[1][0]
two = sortted[0][0]

print(two,"\n",one)  