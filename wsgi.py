import mysql.connector
from flask import Flask

application = Flask(__name__)

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='sampledb')
cnx.close()

@application.route("/")
def hello():
    return "Hello Worldes!"

@application.route("/hello")
def hellos():
    return "Hello da draussen!"

if __name__ == "__main__":
    application.run()
