query = "add 10 and 20 then check weather"

tools = {
    "add": "calculator",
    "weather": "search",
    "news": "search"
}

result = []
for word in query.split():
    if word in tools and tools[word] not in result:
        result.append(tools[word])


for i in result:
    print(i)
