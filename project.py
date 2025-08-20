import re
import datetime
import random
import math

class ChatBot:
    def __init__(self):
        self.rules = [
            # --- GREETINGS & BASIC CHAT ---
            (re.compile(r'hi|hello|hey', re.I), self.greet),
            (re.compile(r'how are you', re.I), self.how_are_you),
            (re.compile(r'what is your name', re.I), self.name),
            (re.compile(r'bye|exit|quit', re.I), self.goodbye),
            (re.compile(r'who created you|who made you', re.I), self.creator),
            (re.compile(r'where are you from', re.I), self.origin),
            (re.compile(r'what can you do', re.I), self.abilities),
            (re.compile(r'tell me about yourself', re.I), self.about_self),
            (re.compile(r'do you like me', re.I), self.like_user),
            (re.compile(r'are you human', re.I), self.are_you_human),

            # --- DATE & TIME ---
            (re.compile(r'what time is it|current time|tell me the time', re.I), self.time),
            (re.compile(r'what is today|today\'s date|date', re.I), self.date),
            (re.compile(r'what day is it', re.I), self.day),
            (re.compile(r'how many days until (.*)', re.I), self.days_until),
            (re.compile(r'year|current year', re.I), self.current_year),

            # --- JOKES, FUN, FACTS ---
            (re.compile(r'tell me a joke|joke', re.I), self.joke),
            (re.compile(r'tell me a riddle|riddle', re.I), self.riddle),
            (re.compile(r'fun fact|interesting fact', re.I), self.fun_fact),
            (re.compile(r'quote|motivation', re.I), self.quote),
            (re.compile(r'give me trivia|trivia', re.I), self.trivia),
            (re.compile(r'who is your favorite superhero', re.I), self.superhero),

            # --- MATH & CALCULATOR ---
            (re.compile(r'([0-9\s\+\-\*\/\(\)\.]+)', re.I), self.solve_math),
            (re.compile(r'square root of (\d+)', re.I), self.square_root),
            (re.compile(r'factorial of (\d+)', re.I), self.factorial),

            # --- GENERAL KNOWLEDGE ---
            (re.compile(r'capital of (.*)', re.I), self.capital_lookup),
            (re.compile(r'who is the president of india', re.I), self.india_president),
            (re.compile(r'who is the prime minister of india', re.I), self.india_pm),
            (re.compile(r'who is the president of usa', re.I), self.usa_president),
            (re.compile(r'who is the prime minister of uk', re.I), self.uk_pm),
            (re.compile(r'largest country', re.I), self.largest_country),
            (re.compile(r'smallest country', re.I), self.smallest_country),
            (re.compile(r'fastest animal', re.I), self.fastest_animal),
            (re.compile(r'tallest building', re.I), self.tallest_building),

            # --- TECHNOLOGY & AI ---
            (re.compile(r'what is ai|artificial intelligence', re.I), self.about_ai),
            (re.compile(r'what is python', re.I), self.about_python),
            (re.compile(r'what is chatgpt', re.I), self.about_chatgpt),
            (re.compile(r'latest technology|trending tech', re.I), self.latest_tech),
            (re.compile(r'what is quantum computing', re.I), self.quantum),
            (re.compile(r'what is machine learning', re.I), self.machine_learning),
            (re.compile(r'what is deep learning', re.I), self.deep_learning),

            # --- SPORTS & ENTERTAINMENT ---
            (re.compile(r'icc world cup winner 2023', re.I), self.cricket_wc2023),
            (re.compile(r'best movie 2025', re.I), self.best_movie_2025),
            (re.compile(r'who won ballon d\'or 2023', re.I), self.ballon_dor),
            (re.compile(r'who won oscar 2024', re.I), self.oscar2024),

            # --- WEATHER (mock answer) ---
            (re.compile(r'weather|temperature', re.I), self.weather),

            # --- DEFAULT ---
            (re.compile(r'.*', re.I), self.default_response)
        ]

    # --- BASIC RESPONSES ---
    def greet(self, _):
        return random.choice(["Hello! How can I assist you today?", "Hi there 👋 What can I do for you?", "Hey! Need any help?"])
    def how_are_you(self, _): return "I'm doing great (for a chatbot)! How about you?"
    def name(self, _): return "I'm your friendly chatbot, here to assist you with any questions you have."
    def goodbye(self, _): return "Goodbye! Have a great day!"
    def creator(self, _): return "I was created by a programmer (like you!) using Python."
    def origin(self, _): return "I live inside your computer, in the magical world of Python code!"
    def abilities(self, _): return "I can chat, tell time, date, jokes, solve math, share facts, and answer knowledge questions!"
    def about_self(self, _): return "I'm a rule-based chatbot made in Python."
    def like_user(self, _): return "Of course I like chatting with you!"
    def are_you_human(self, _): return "No, I'm an AI chatbot, not a human."

    # --- DATE & TIME ---
    def time(self, _): return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    def date(self, _): return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}."
    def day(self, _): return f"Today is {datetime.date.today().strftime('%A')}."
    def days_until(self, match):
        try:
            event = match.group(1)
            today = datetime.date.today()
            target = datetime.datetime.strptime(event.strip()+" "+str(today.year), "%B %d %Y").date()
            delta = (target - today).days
            if delta >= 0: return f"There are {delta} days until {event}."
            else: return f"{event} already passed this year."
        except: return "Sorry, I couldn't calculate. Try format: 'how many days until December 25'."
    def current_year(self, _): return f"The current year is {datetime.date.today().year}."

    # --- FUN ---
    def joke(self, _):
        return random.choice([
            "Why don't programmers like nature? Too many bugs!",
            "Why do Java developers wear glasses? Because they don't see sharp!",
            "What's a computer's favorite snack? Microchips!",
            "Why did the AI cross the road? To optimize the chicken's path!",
            "Parallel lines have so much in common. It's a shame they'll never meet."

        ])
    def riddle(self, _):
        return random.choice([
            "I speak without a mouth and hear without ears. What am I? (Echo)",
            "What has keys but can't open locks? (Piano)",
            "The more you take, the more you leave behind. (Footsteps)"
        ])
    def fun_fact(self, _):
        return random.choice([
            "The first computer virus was created in 1986, called 'Brain'.",
            "The first 1GB hard disk was announced in 1980 and weighed over 500 pounds!",
            "ChatGPT reached 100M users in 2 months in 2023!",
            "The year 2025 is the International Year of Quantum Science and Technology."
        ])
    def quote(self, _):
        return random.choice([
            "The best way to predict the future is to invent it. – Alan Kay",
            "Talk is cheap. Show me the code. – Linus Torvalds",
            "Stay hungry, stay foolish. – Steve Jobs"
        ])
    def trivia(self, _):
        return random.choice([
            "The human brain has about 86 billion neurons.",
            "Bananas are berries, but strawberries are not!",
            "Octopuses have three hearts.",
            "Sharks existed before trees."
        ])
    def superhero(self, _): return "I like Iron Man. He reminds me of advanced technology!"

    # --- MATH ---
    def solve_math(self, match):
        try: return f"The answer is {eval(match.group(1))}"
        except: return None
    def square_root(self, match): return f"The square root of {match.group(1)} is {math.sqrt(int(match.group(1)))}"
    def factorial(self, match): return f"The factorial of {match.group(1)} is {math.factorial(int(match.group(1)))}"

    # --- GENERAL KNOWLEDGE ---
    def capital_lookup(self, match):
        c = match.group(1).strip().lower()
        caps = {"india": "New Delhi", "usa": "Washington, D.C.", "japan": "Tokyo", "france": "Paris", "china": "Beijing", "uk": "London"}
        return f"The capital of {c.title()} is {caps[c]}" if c in caps else f"Sorry, I don't know the capital of {c}."
    def india_president(self, _): return "As of 2025, the President of India is Droupadi Murmu."
    def india_pm(self, _): return "As of 2025, the Prime Minister of India is Narendra Modi."
    def usa_president(self, _): return "As of 2025, the President of USA is Joe Biden."
    def uk_pm(self, _): return "As of 2025, the Prime Minister of UK is Rishi Sunak."
    def largest_country(self, _): return "The largest country in the world by area is Russia."
    def smallest_country(self, _): return "The smallest country in the world is Vatican City."
    def fastest_animal(self, _): return "The fastest land animal is the cheetah."
    def tallest_building(self, _): return "The tallest building as of 2025 is Burj Khalifa in Dubai."

    # --- TECH ---
    def about_ai(self, _): return "AI simulates human intelligence in machines to think, learn, and decide."
    def about_python(self, _): return "Python is a high-level language known for simplicity."
    def about_chatgpt(self, _): return "ChatGPT is an AI model developed by OpenAI."
    def latest_tech(self, _): return "Trending tech 2025: Quantum Computing, AI Agents, 6G, EVs, Space Tech."
    def quantum(self, _): return "Quantum computing uses quantum mechanics to perform computations much faster."
    def machine_learning(self, _): return "Machine Learning is teaching machines to learn from data without explicit programming."
    def deep_learning(self, _): return "Deep Learning is a subset of ML using neural networks with many layers."

    # --- SPORTS & ENTERTAINMENT ---
    def cricket_wc2023(self, _): return "Australia won the ICC Cricket World Cup 2023 by defeating India."
    def best_movie_2025(self, _): return "Dune: Part Two is one of the top-rated movies in 2025."
    def ballon_dor(self, _): return "Lionel Messi won the Ballon d'Or in 2023."
    def oscar2024(self, _): return "Oppenheimer won multiple Oscars in 2024 including Best Picture."

    # --- WEATHER ---
    def weather(self, _): return "I can't fetch live weather, please check a weather app."

    # --- DEFAULT ---
    def default_response(self, _): return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def respond(self, user_input):
        for pattern, func in self.rules:
            match = pattern.match(user_input)
            if match:
                response = func(match)
                if response: return response
        return self.default_response(user_input)


def main():
    bot = ChatBot()
    print("ChatBot: Hi! I'm your chatbot. Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye','exit','quit']:
            print("ChatBot: Goodbye! Have a great day!")
            break
        print(f"ChatBot: {bot.respond(user_input)}")

if __name__ == "__main__":
    main()
