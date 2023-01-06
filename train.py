from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import json

##Makes the bot work for some reason
##https://stackoverflow.com/a/69802850
import time
time.clock = time.time

chatbot = ChatBot("Klarabot")
trainer = ListTrainer(chatbot)

with open('training_data/training_data.json') as training_data:
    print ('Loading data...')
    try:
        data = json.load(training_data)
        for intent in data:
            print (f"Intent-Tag: {intent['tag']}")
            for pattern in intent['patterns']:
                for response in intent['responses']:
                    print ([pattern, response])
                    ##Effectively Train Data
                    trainer.train([pattern, response])
    except:
        print('Training Data could not be loaded.')
    

#Corpus
#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.german")