Chatty: A Simple NLP Chatbot
Chatty is a basic chatbot built using Python, spaCy, and a JSON-based intent system. It uses natural language processing to understand user inputs and respond with pre-defined messages based on intents.



Features:
NLP with spaCy: Utilizes the spaCy library to process user input and understand the meaning of words.
Intent Matching: The bot matches user input to pre-defined intents from a JSON file to provide relevant responses.
Dynamic Responses: Responses are chosen randomly from a list of possible replies for each matched intent.
Exit Condition: The chatbot can be easily shut down by typing "exit" or "quit."



How It Works:
The chatbot takes user input.
It uses spaCy to analyze the input and checks if it matches any phrases in the intent file (intents.json).
If a match is found, the bot selects a response from the corresponding intent.
If no match is found, the bot replies with a default response asking for clarification.



Usage
Run the chatbot by clicking on the windows batch file.
Chat with the bot in the terminal by typing your queries.
To exit the chat, type exit or quit.
