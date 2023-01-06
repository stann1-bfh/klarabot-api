from chatterbot import ChatBot

# Deleting all Data for the Chatbot
def dumpChatbot(chatbot: ChatBot):
    chatbot.storage.drop()