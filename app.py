from tool.tools import ask_agent

print("="*70)
print("🇧🇩 Bangladesh Multi-Tool AI Agent")
print("="*70)

print("""
Available Tools

1. Hospital Database
2. Institution Database
3. Restaurant Database
4. DuckDuckGo Web Search
""")

print("Type exit to stop.\n")

while True:

    question = input("User : ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    try:

        answer = ask_agent(question)

        print("\nAssistant:\n")

        print(answer)

        print("\n" + "="*70 + "\n")

    except Exception as e:

        print(e)