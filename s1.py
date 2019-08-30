# Author: Aniketh S Deshpande
# Flask-Server
# MongoDB Database 

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/q"
api = Api(app)
mongo = PyMongo(app)


class Q_entries(Resource):
    def get(self):
        q_array = []
        for item in mongo.db.q.find():
            q_array.append([item['name'],  int(item['size']), int(item['skip_count'])])
        return {'queue': q_array}


# resources routing
api.add_resource(Q_entries, '/q_entries')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.27')

