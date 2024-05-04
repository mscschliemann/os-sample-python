from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Worldes!"

@application.route("/hello")
def hello():
    return "Hello da draussen!"

if __name__ == "__main__":
    application.run()
