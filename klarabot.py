from chatterbot import ChatBot
from os import system, name as systemName

import time 
time.clock = time.time
chatbot = ""

def initChatBot(name):
    global chatbot
    chatbot = ChatBot(
        name,
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                'input_text': 'empty',
                'output_text': 'SpecResponse'
            },
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default-response': 'Entschuldige, ich verstehe nicht was du meinst, ich Frage bei den Kollegen nach.',
                'maximum_similarity_threshold': 0.90
            }
        ],
        read_only = True,
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.unescape_html',
            'chatterbot.preprocessors.convert_to_ascii'
        ]
    )
    
def getChatBot(name):
    global chatbot
    if chatbot.name == name:
        return chatbot