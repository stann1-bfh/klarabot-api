from chatterbot import ChatBot

##Makes the bot work for some reason
##https://stackoverflow.com/a/69802850
import time
time.clock = time.time

chatbot = ChatBot("Klarabot")
chatbot.storage.drop()