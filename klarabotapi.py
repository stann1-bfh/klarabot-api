from flask import Flask, request
from flask_restful import Resource, Api, reqparse, MethodView
from chatterbot import ChatBot
import json, ast, time
from klarabot import *

#Initialize Flask API
app = Flask(__name__)
api = Api(app)

##Makes the bot work for some reason
##https://stackoverflow.com/a/69802850
time.clock = time.time
initChatBot("Klarabot")
chatbot = getChatBot("Klarabot") 

class KlarabotAPI(MethodView):
    def get(self):
        query = request.args.get("message")
        response = chatbot.get_response(query)
        data = {'message': str(response), 'confidence': response.confidence}
        return (data), 200

##Config API Paths
api.add_resource(KlarabotAPI, '/klarabotapi')

@app.route('/')
def index():
    #Define welcoming Page
    return "<h1>Welcome to the Klarabot-API</h1><p>This is a work in progress.</p>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)