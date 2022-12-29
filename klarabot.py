from chatterbot import ChatBot
from os import system, name as systemName

import time 
time.clock = time.time
chatbot = ""

def initChatBot(name):
    global chatbot
    chatbot = ChatBot(
        name,
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default-response': 'Entschuldige, ich verstehe nicht was du meinst, ich Frage bei den Kollegen nach.'
            }
        ]
    )
    
def getChatBot(name):
    global chatbot
    if chatbot.name == name:
        return chatbot