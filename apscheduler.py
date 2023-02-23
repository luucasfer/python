import requests, json, threading
from time import sleep
from apscheduler.schedulers.background import BlockingScheduler, BackgroundScheduler
from datetime import datetime

# CREATES A DEFAULT BACKGROUND SCHEDULER
sched = BlockingScheduler()
#sched = BackgroundScheduler(daemon=True)



#CAPTURE ALL SCHEDULES SAVED AT mySQL
def getAllSchedulesFromMYSQL():
    requestToAPI = requests.get("http api link")
    gettingContentFromRequest = requestToAPI.content
    APIcontentAsDictonary = json.loads(gettingContentFromRequest)
    APIcontentAsDictonary = APIcontentAsDictonary["data"]
    return APIcontentAsDictonary


#VERIFY WHICH SCHEDULES HAVE "STATUS == TRUE"
#{"device": "test", "data": "2022-12-12", "scheduleStart": "10:09:00", "scheduleEnd": "10:10:00", "status": true}
def verifyScheduleEnable():
    global actualDevice, dateNormalizedTurnOn

    allSchedulesData = getAllSchedulesFromMYSQL()
    allSchedulesLength = len(allSchedulesData)
    dictPosititon = 0

    while dictPosititon < allSchedulesLength:
        if 'status' in allSchedulesData[dictPosititon].keys(): 
            if True in allSchedulesData[dictPosititon].values():
                actualDevice  = allSchedulesData[dictPosititon]["device"]
                yearMonthDay  = allSchedulesData[dictPosititon]["date"]
                scheduleStart = allSchedulesData[dictPosititon]["scheduleStart"]
                scheduleEnd   = allSchedulesData[dictPosititon]["scheduleEnd"]
                
                #Formated as (2022-12-08 10:48:10)
                dateNormalizedTurnOn  = (yearMonthDay[0:4] + "-" + yearMonthDay[5:7] + "-" + yearMonthDay[8:10] + " " + scheduleStart)
                dateNormalizedTurnOff = (yearMonthDay[0:4] + "-" + yearMonthDay[5:7] + "-" + yearMonthDay[8:10] + " " + scheduleEnd)

                print(
                    {"message":[ 
                        f'SCHEDULE HOURS ENABLE AT: {actualDevice}',
                        f'TURN ON TIMER: {dateNormalizedTurnOn}',
                        f'TURN OFF TIMER: {dateNormalizedTurnOff}'
                    ]}
                    )
                
                sched.add_job(postTurnOnPayload, 'date', run_date = dateNormalizedTurnOn, args=[actualDevice])
                sched.add_job(postTurnOffPayload, 'date', run_date = dateNormalizedTurnOff, args=[actualDevice])
                
                
            dictPosititon += 1
    

        
                    

#DEFINE PAYLOADS TO POST IN THE AUTOMATION ROUTE
#payload example = {"lamp1":true, "devices":["FARMSTECH-POSTE1"]} 
def postTurnOnPayload(device):
    now = datetime.now()
    payload = {"allLamps":True, "devices":[device]}
    print(f"Agora é: {now} -> ", payload)
    url = "http api link"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(url, data=payload, headers=headers)

def postTurnOffPayload(device):
    now = datetime.now()
    payload = {"allLamps":False, "devices":[device]}
    print(f"Agora é: {now} -> ", payload)
    url = "http api link"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    requests.post(url, data=payload, headers=headers)


    




if __name__ == "__main__":
    verifyScheduleEnable()
    sched.start()
