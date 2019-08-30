# Author: Aniketh S Deshpande
# Flask-Server

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# f is a flower name
q = {
    "f1": {
        "size": 4,
        "skip_count": 0
    },
    "f2": {
        "size": 8,
        "skip_count": 1
    },
    "f3": {
        "size": 5,
        "skip_count": 0
    }
}

class Q_entries(Resource):
    global q
    def get(self):
        return q
    
    def post(self):
        new_flower = request.get_json()
        return {'your_details': new_flower}

# resources routing
api.add_resource(Q_entries, '/q_entries')

if __name__ == '__main__':
    app.run(debug=True)

