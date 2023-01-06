from chatterbot import ChatBot

def dumpChatbot(chatbot: ChatBot):
    chatbot.storage.drop()