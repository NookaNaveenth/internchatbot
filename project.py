import re

class ChatBot:
    def __init__(self):
        self.rules = [
            (re.compile(r'hi|hello', re.I), self.greet),
            (re.compile(r'how are you', re.I), self.how_are_you),
            (re.compile(r'what is your name', re.I), self.name),
            (re.compile(r'bye|exit', re.I), self.goodbye),
            (re.compile(r'.*', re.I), self.default_response)  # Default response for any other input
        ]

    def greet(self, _):
        return "Hello! How can I assist you today?"

    def how_are_you(self, _):
        return "I'm just a bunch of code, but I'm here to help you!"

    def name(self, _):
        return "I'm your friendly chatbot, here to assist you with any questions you have."

    def goodbye(self, _):
        return "Goodbye! Have a great day!"

    def default_response(self, _):
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def respond(self, user_input):
        for pattern, response_function in self.rules:
            if pattern.match(user_input):
                return response_function(user_input)
        return self.default_response(user_input)

def main():
    bot = ChatBot()
    print("ChatBot: Hi! I'm your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit']:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = bot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
