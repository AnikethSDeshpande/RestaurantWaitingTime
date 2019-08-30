# Author: Aniketh S Deshpande
# Flask-Server

from flask import Flask, Request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# f is a flower name
q = {
    "f1": {
        "size": 4
    }
}

class Q_insert(Resource):
    global q
    def get(self):
        return q

# resources routing
api.add_resource(Q_insert, '/q_insert')

if __name__ == '__main__':
    app.run(debug=True)

