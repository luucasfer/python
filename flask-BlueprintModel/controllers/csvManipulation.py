from models.mongodb import db
from flask_smorest import Blueprint
from flask import request, jsonify, send_file
import csv


csvManipulation = Blueprint("CSV", __name__)




@csvManipulation.route('/readCSV', methods=['POST'])
def readCSV():
    try:
        gettingCSV = request.files["filename"]
        file_read = gettingCSV.stream.read()
        csvDecoded = file_read.decode('UTF-8')
        csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(csvDecoded.splitlines(), skipinitialspace=True)]

        csvList = []
        for eachDict in csv_dicts:
            csvList.append(eachDict)

        return {"FL_STATUS": True, "data": csvList}

    except Exception as e:
        return jsonify({'FL_STATUS': False, 'message': f'Error: {e}'})





@csvManipulation.route('/exportCSV', methods=['GET'])
def exportingCSV():
    try:

        header = ['put headers here, separated by comma']
        data = []

        with open('./path/to/file.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)

        return send_file('./path/to/file.csv',
            mimetype='text/csv',
            download_name='archiveName.csv',
            as_attachment=True)

    except Exception as e:
        return jsonify({'FL_STATUS': False, 'data': e})
