import random
import spacy
import json

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load intents from JSON file
with open('intents.json', 'r') as file:
    intents = json.load(file)

# Function to get a response based on the user's input
def get_response(user_input):
    doc = nlp(user_input.lower())

    for intent in intents['intents']:
        for phrase in intent['inputs']:
            if phrase.lower() == user_input.lower():
                return random.choice(intent['response'])

    # Iterate over intents and check if any input matches
    for intent in intents['intents']:
        if any(token.lemma_ in intent['inputs'] for token in doc):
            return random.choice(intent['response'])

    # If no match is found, return a default response
    return "I'm sorry, I didn't quite get that. Could you please rephrase?"

# Chat loop
def chat():
    print("Chatty: Hello! I'm Chatty. How can I assist you today?")

    while True:
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() in ['exit', 'quit']:
            print(f"Chatty: Shutting down Chatty")
            break

        # Get bot response
        response = get_response(user_input)
        print(f"Chatty: {response}")

# Run the chatbot
chat()

