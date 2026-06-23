print("Welcome to Simple Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")
    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")
    elif user == "how are you":
        print("Bot: I am doing well. Thank you!")
    elif user == "what is your name":
        print("Bot: I am a simple Python chatbot.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
