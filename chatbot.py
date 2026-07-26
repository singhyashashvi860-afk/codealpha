def get_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

def chat():
    print("Chatbot: Hi! Type 'bye' to end our chat.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    chat()