from flask import Blueprint, request
from datetime import datetime


basicCrud = Blueprint("SimpleCRUD", __name__)

now = datetime.now()



@basicCrud.route("/register", methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        "script"


        return {'message': "REGISTERED with success", 'FL_STATUS': True}
    except Exception as e:
        return {"message": str(e), 'FL_STATUS': False}



@basicCrud.route("/read", methods=['GET'])
def read():
    try:
        f = open("./app/config.json")
        data = f.read()
        "script"

        return {"data": data, 'FL_STATUS': True}
    except Exception as e:
        return {"message": str(e), 'FL_STATUS': False}



@basicCrud.route("/update", methods=['PUT'])
def update():
    try:
        data = request.get_json()
        
        "script"

        return {"message": "Data UPDATED with success", 'FL_STATUS': True}
    except Exception as e:
        return {"message": str(e), 'FL_STATUS': False}



@basicCrud.route("/delete", methods=['DELETE'])
def delete():
    try:
        data = request.get_json()

        "script"

        return {'message': "Data DELETED", 'FL_STATUS': True}

    except Exception as e:
        return {"message": str(e), 'FL_STATUS': False}

