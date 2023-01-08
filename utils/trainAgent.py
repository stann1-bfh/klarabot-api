from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot
import json, yaml
import traceback

##Makes the bot work for some reason
##https://stackoverflow.com/a/69802850
import time
time.clock = time.time

# Training the Chatterbot with a JSON-Formatted File
def trainWithJson(path, trainer: ListTrainer):
    with open(path, encoding="utf-8") as training_data:
        try:
            data = json.load(training_data)
            for intent in data:
                print (f"Intent-Tag: {intent['tag']}")
                for pattern in intent['patterns']:
                    for response in intent['responses']:
                        ##Effectively Train Data
                        trainer.train([pattern, response])
        except:
            print('Training Data could not be loaded.')

# Training the ChatterBot with a Corpus-Data Formatted file
def trainWithYaml(path, trainer: ChatterBotCorpusTrainer):
    try:
        trainer.train(path)
    except Exception as exception:
        print('Training Date could not be loaded.')
        traceback.print_exc()