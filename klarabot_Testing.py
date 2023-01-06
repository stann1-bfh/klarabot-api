from chatterbot import ChatBot
from os import system, name as systemName

##Makes the bot work for some reason
##https://stackoverflow.com/a/69802850
import time 
time.clock = time.time

chatbot = ChatBot("Klarabot")

exit_conditions = (":q", "quit", "exit")

# Clear cmd
if systemName == 'nt':
    _ = system('cls')
else:
    _ = system('clear')
        
print(f"{chatbot.name} initialized")
while True:  
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        print(f"Klarabot: {response}")
        print(f"Confidence value: {response.confidence}")