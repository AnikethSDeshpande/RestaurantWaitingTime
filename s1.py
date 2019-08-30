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
    },
    "f2": {
        "size": 8
    }
}

class Q_entries(Resource):
    global q
    def get(self):
        return q

# resources routing
api.add_resource(Q_entries, '/q_entries')

if __name__ == '__main__':
    app.run(debug=True)

