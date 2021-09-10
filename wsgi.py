from flask import Flask
from flask import Response
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/text/plain")
def text_plain():
    return Response("Hello World!", mimetype='text/plain')

if __name__ == "__main__":
    application.run()
