from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from os import system, name as systemName, listdir
from os.path import isfile, join
import utils.trainAgent as trainAgent
import utils.dumpAgent as dumpAgent
import sys

##Makes the bot work for some reason
##https://stackoverflow.com/a/69802850
import time 
time.clock = time.time

if __name__ == "__main__":
    chatbot = ChatBot("Klarabot")
    trainer = ListTrainer(chatbot)
    corpusTrainer = ChatterBotCorpusTrainer(chatbot)

    # Clear cmd
    if systemName == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
            
    if (sys.argv[1] == "dump"):
        print (f"Starting to dump data for {chatbot.name}")
        dumpAgent.dumpChatbot(chatbot)
    else:
        print(f"{chatbot.name} initialized, starting Training")
        mypath = "processed_training_data"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for file in onlyfiles:
            if "yaml" in file:
                trainAgent.trainWithYaml(f"{mypath}/{file}", corpusTrainer)
            elif "json" in file:
                trainAgent.trainWithJson(f"{mypath}/{file}", trainer)
            else:
                print(F"Skipping {file}, because it's not a Training data file!")