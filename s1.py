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
            q_array.append([item['name'],  int(item['size']), int(item['skip_count']), int(item['position']) ])
        return {'queue': q_array}
    
    def post(self):
        obj = request.get_json(force=True)
        mongo.db.q.insert(obj)
        return {'object_posted': str(obj)}

    def update(self):
        obj = request.get_json(force=True)
        name, new_skip_count, new_position = obj['name'], obj['new_skip_count'], obj['new_position']
        mongo.db.q.update({'name': name}, {'$set':{'skip_count': new_skip_count, 'position': new_position}})
        return {'object_updated': str(obj)}
        
    def delete(self):
        obj = request.get_json(force=True)
        name = obj['name']
        mongo.db.q.delete({'name': name})
        return {'object_deleted': str(obj)}




# resources routing
api.add_resource(Q_entries, '/q_entries')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.27')

