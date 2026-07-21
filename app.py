from rag import chain

print("---------------Company Policy Assistant---------------")
print("---------------Press 0 to Exit---------------")

while True:
    query = input("You: ")
    if query == "0":
        break
    response = chain.invoke(query)
    print(response)
