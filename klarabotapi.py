from flask import Flask, request
from flask_restful import Api, MethodView
from flask_cors import CORS
from klarabot import *
import time

#Initialize Flask API
app = Flask(__name__)
api = Api(app)
#Enable Cross Origin Resource Sharing
CORS(app)

##Makes the bot work for some reason
##TODO: Try to remove this.
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

##Config Default Path to Index-Website
@app.route('/')
def index():
    #Define welcoming Page
    return "<h1>Welcome to the Klarabot-API</h1><p>This is a work in progress.</p>"

##Config API Paths
api.add_resource(KlarabotAPI, '/klarabotapi')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)