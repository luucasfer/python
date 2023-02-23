from flask import Blueprint, request, jsonify
import json


statusJson = Blueprint("statusJson", __name__)


#poles_list = ['FARMSTECH-POSTE1', 'FARMSTECH-POSTE2', 'FARMSTECH-POSTE3', 'FARMSTECH-POSTE4']
#json_position = ['POLE01','POLE02','POLE03','POLE04']
polesQuantity = 5
poles_list = ["FARMSTECH-POSTE" + str(poles) for poles in range(1,polesQuantity)] 
json_position = ["POLE0" + str(poles) for poles in range(1,polesQuantity)] 



#WRITE TELEMETRIES AT status.JSON
@statusJson.route("/write", methods=['POST'])
def postStates():
    global poles_list, json_position

    telemetry = request.get_json()
    #print(type(telemetry))

    position = 0
    while position < len(poles_list):           #ITERATE ALL THE POLES FROM poles_list = []
        try:
            if telemetry["device"] in [poles_list[position]]:        #IF THE {VALUE} OF THE RECEIVED TELEMETRY IS "FARMSTECH-POSTEx" AT {KEY} "device" IT ENTERS THE if
                print(f"#### TELEMTRY RECEIVED FROM {poles_list[position]}... STATUS.JSON UPDATED ####")
                with open("./app/status.json", "r+") as jsonFile:              # r+  OPEN IN THE UPDATE MODE
                    data = json.load(jsonFile)
                    data[json_position[position]].update(telemetry)      #IDENTIFY THE LOCATION WHERE IT WILL UPDATE, IN THIS CASE, ALL THE STRUCTURE INSIDE THE {POLE0x}
                    jsonFile.seek(0)                                     #GO TO THE FIRST JSON LINE
                    json.dump(data, jsonFile, indent=4)                  #PUT THE data IN THE JSONfile WITH THE INDENT OF JSON
                    jsonFile.truncate()   
                    break
            else:                                                 
                position = position + 1     
        except:
            None
    return telemetry   



#READ TELEMETRIES FROM status.JSON TO UPDATE THE FRONTEND
@statusJson.route("/read", methods=['GET'])
def getStates():
    f = open("./app/status.json")
    data = f.read()
    print(data)
    return jsonify(json.loads(data))
