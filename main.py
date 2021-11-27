import os
from wsgiref import simple_server

from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    return "Flask app is running and I am changing something"

port = int(os.getenv("PORT", 5001))


if __name__ == "__main__":
    host = '0.0.0.0'
    # app.run(host="0.0.0.0",port=5000)
    httpd = simple_server.make_server(host=host, port=port, app=app)
    httpd.serve_forever()