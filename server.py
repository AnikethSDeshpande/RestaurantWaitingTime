# Author: Aniketh S Deshpande
# API for Queue
# Flask-Server
# MongoDB Database 

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_cors import CORS

from best_fit import bestFit

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/q"
api = Api(app)
mongo = PyMongo(app)

# Q-API
class Q_entries(Resource):
    def get(self):
        q_array = []
        for item in mongo.db.q.find():
            q_array.append([item['name'],  int(item['size']), int(item['skip_count']), int(item['position']), item['contact_details'] ])
        return {'queue': q_array}
    
    def post(self):
        obj = request.get_json(force=True)
        mongo.db.q.insert(obj)
        return {'obj': str(obj)}, 200

    def update(self):
        obj = request.get_json(force=True)
        name, new_skip_count, new_position = obj['name'], obj['new_skip_count'], obj['new_position']
        mongo.db.q.update({'name': name}, {'$set':{'skip_count': new_skip_count, 'position': new_position}})
        return {'object_updated': obj}
        
    def delete(self):
        obj = request.get_json(force=True)
        name = obj['name']
        mongo.db.q.delete({'name': name})
        return {'object_deleted': str(obj)}


# Tables-API

class T_entries(Resource):
    def get(self):
        t_array = []
        for item in mongo.db.t.find():
            t_array.append([item['number'],  int(item['size']), int(item['occupancy']) ])
        return {'table': t_array}
    
    def post(self):
        obj = request.get_json(force=True)
        mongo.db.t.insert(obj)
        return {'object_posted': str(obj)}

    def update(self):
        obj = request.get_json(force=True)
        number, new_size, new_occupancy = obj['number'], obj['new_size'], obj['new_occupancy']
        mongo.db.t.update({'number': number}, {'$set':{'occupancy': new_occupancy}})
        return {'object_updated': str(obj)}
        
    def delete(self):
        obj = request.get_json(force=True)
        name = obj['name']
        mongo.db.q.delete({'name': name})
        return {'object_deleted': str(obj)}

'''
class getQ(Resource):
    # we intend to get the groups that end up in Queue
    def get(self):
        result = bestFit(tables, table_size, group, group_size)
'''        
# resources routing
api.add_resource(Q_entries, '/q_entries')
api.add_resource(T_entries, '/t_entries')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.27')
