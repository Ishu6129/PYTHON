from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

# Start a conversation with the chatbot
print("Welcome to MyChatBot. Ask me anything or say 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("MyChatBot: Goodbye! Have a great day!")
        break
    else:
        response = chatbot.get_response(user_input)
        print("MyChatBot:", response)
