print("🤖AI CHATBOT!!!" )
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user== "hi":
        print("Bot: Hello! Welcome 😊 ")

    elif user == "what is your name":
        print("Bot: I'm CodSoft AI Chatbot.")

    elif user == "how are you":
        print("Bot: I'm doing great!")

    elif user == "study":
        print("Bot: Study daily for improving your skills.")

    elif user == "what is python":
        print("Bot:  Python is a high-level programming language known for its simple, highly readable syntax.")

    elif user == "motivate":
        print("Bot: Believe in yourself and keep learning!")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day 😊")
        break

    else:
        print("Bot: Sorry, I don't understand.")