from flask import Flask
from flask import Response
from flask_cors import CORS, cross_origin

application = Flask(__name__)
CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/text/plain")
def text_plain():
    return Response("Hello World!", mimetype='text/plain')

if __name__ == "__main__":    
    application.run()

