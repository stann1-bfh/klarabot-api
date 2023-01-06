from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from os import system, name as systemName
import utils.trainAgent as trainAgent
import utils.dumpAgent as dumpAgent

##Makes the bot work for some reason
##https://stackoverflow.com/a/69802850
import time 
time.clock = time.time

if __name__ == '__main__':
    chatbot = ChatBot("Klarabot")
    trainer = ListTrainer(chatbot)
    corpusTrainer = ChatterBotCorpusTrainer(chatbot)
    exit_conditions = (":q", "quit", "exit")

    # Clear cmd
    if systemName == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
            
    print(f"{chatbot.name} initialized, starting Training")
    print('Dumping previous data')
    dumpAgent.dumpChatbot(chatbot)
    trainAgent.trainWithYaml('training_data/training_data_papr001.yaml', corpusTrainer)