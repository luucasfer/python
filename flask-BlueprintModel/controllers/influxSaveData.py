from flask import Blueprint, request
from influxdb import InfluxDBClient
from models.influxdb import client
import datetime



influx = Blueprint("influxDB", __name__)


#SEND DATA TO INFLUXDB
@influx.route("/influxDB", methods=['POST'])
def sendToInflux():

    telemetry = request.get_json()

    try:
        client.switch_database('database influx name')

        #FOR EACH METRIC IT GENERATES A SEPARATE TABLE AT INFLUX
        metrics = ["lamp1","lamp2","Temp_Device"]   

        for datas in telemetry:
            if datas in metrics:
                json_body = [
                    {
                        "measurement": datas,
                        "tags": {
                            "device": telemetry["device"],                
                        },
                        "time": datetime.datetime.now(),
                        "fields":{
                            "value":telemetry[datas]
                        }
                    }
                ]
                client.write_points(json_body)
                print({'message': 'data saved at influx'})
            else:
                pass
    except Exception as e:
        print("Error: ",e)
    return telemetry