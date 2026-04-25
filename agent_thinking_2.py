query = "what is weather today"

tools = {
    "add": "calculator",
    "weather": "search",
    "news": "search"
}
result = "search"

for words in query.split():
    if words in tools:
        result = tools[words]
        break

print(result)