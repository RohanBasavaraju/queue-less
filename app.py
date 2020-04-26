import json
import db
from flask import Flask, request

app = Flask(__name__)
Db = db.DB()

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5000, debug=True)
