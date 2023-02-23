from models.mongodb import db
from flask_smorest import Blueprint
from flask import request, jsonify


mongoDBCRUD = Blueprint("mongoCRUD", __name__)




@mongoDBCRUD.route('/insertOne', methods=['GET', 'POST'])
def insert():
    data = request.get_json()
    try:
        collection = db['Collection']
        collection.insert_one(data)
    except Exception as e:
        print('Except: Impossible to save in MongoDB', f"Error: {e}")




@mongoDBCRUD.route('/find', methods=['GET', 'POST'])
def find():
    data = request.get_json()

    try:
        collection = db['Collection']
        document = collection.find(
            filter = {
                "$and": [
                    {"key1": ""},
                    {"key2": ""},
                ]
            },
            projection = {
                "key3":1,
                "_id":0, 
            } 
        )

        docToReturn = []
        for eachData in document:
            docToReturn.append(eachData['key3'])

        return {'FL_STATUS': True, 'data': docToReturn}
    except Exception as e:
        return jsonify({'FL_STATUS': False, 'data': e})




@mongoDBCRUD.route('/update', methods=['PUT'])
def update():
    try:
        data= request.get_json()

        collection = db['Collection']
        collection.update_one(
            {
                "$and": [
                    {"key1": ""},
                    {"key2": ""},
                ]
            },
            {"$set": {
                "DATETIME":  datetime.now(),
                } 
            }
        )
        return {'FL_STATUS': True, 'data': 'updated with success'}
    except Exception as e:
        return jsonify({'FL_STATUS': False, 'data': e})



@mongoDBCRUD.route('/delete', methods=['DELETE'])
def update():
    try:
        data= request.get_json()

        collection = db['Collection']
        collection.delete_one(
            {
                "$and": [
                    {"key": "value"},
                ]
            }   
        )

        return {'FL_STATUS': True, 'data': 'Deleted with success'}
    except Exception as e:
        return jsonify({'FL_STATUS': False, 'data': e})