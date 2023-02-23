import json
from time import sleep

# EXEMPLOS DE TELEMETRIAS QUE CHEGAM
a = {"sensorname": ["FARMSTECH-POSTE1","FARMSTECH-POSTE2"], "Lampada1": 1, "Lampada2": 1, "Temperatura_ESP32": 55555, "time": 1764535}
b = {"sensorname": ["FARMSTECH-POSTE2"], "Lampada1": 1, "Lampada2": 1, "Temperatura_ESP32": 51, "time": 1764535}
c = {"sensorname": "FARMSTECH-POSTE3", "Lampada1": 1, "Lampada2": 1, "Temperatura_ESP32": 52, "time": 1764535}
d = {"sensorname": "FARMSTECH-POSTE4", "Lampada1": 1, "Lampada2": 1, "Temperatura_ESP32": 53, "time": 1764535}

poles_list = []
json_position = []
for poles in range(1,5):
    poles_list.append("FARMSTECH-POSTE" + str(poles))
    json_position.append("POSTE0" + str(poles))

def quebra_payload(telemetry):
        position = 0
        qtd_devices = len(telemetry["sensorname"])
        print("QUANTIDADE DE DEVICES NO PAYLOAD =", qtd_devices)
        while position < qtd_devices:
            try:  
                if qtd_devices > 1:  
                    telemetry["sensorname"] = poles_list[position]    
                    print("\n")            
                    print(f"PAYLOAD PARCIAL =  {telemetry}")
                    print(f"Enviando telemetria pro {poles_list[position]}...")
                    sleep(4)
                    position = position + 1
                else:
                    print("\n")               
                    print(telemetry)
                    sensorname = "sensorname"
                    print(f"Enviando telemetria pro {telemetry[sensorname]}...")
                    break
            except:
                None 


def atualiza_json(telemetry):
        position = 0
        while position < len(poles_list):
            print(f'"{poles_list[position]}"')
            print(json_position[position])
            #telemetry = str(telemetry)
            try:
                if telemetry["sensorname"] in [poles_list[position]]:    #ENTRA NO IF SE A TELEMETRIA RECEBIDA ESTIVER ESCRITO "FARMSTECH-POSTEx" na chave "sensorname"
                    print("telemetria recebida é deste poste, atualiza o json")
                    with open("status.json", "r+") as jsonFile:
                        data = json.load(jsonFile)
                        data[json_position[position]].update(telemetry)      #IDENTIFICA O LOCAL QUE SERÁ FEITO A ATUALIZAÇÃO, NO CASO, TODA ESTRUTURA DENTRO DAS CHAVES DE {POSTE0x}
                        jsonFile.seek(0)                                     #VOLTA PRA PRIMEIRA LINHA DO JSON
                        json.dump(data, jsonFile, indent=4)                  #POE OS DADOS ATUALIZADO NO JSONfile COM IDENTAÇÃO DE UMA ESTRUTURA JSON
                        jsonFile.truncate()   
                        break
                else:
                    print("telemetria não é deste poste")
                    position = position + 1     
            except:
                None                        






#PARA FINS DE TESTE JOGUE NESTA FUNÇÃO AS TELEMETRIAS a,b,c ou d
#VOCÊ OBSERVARÁ QUE O JSON É ATUALIZADO APENAS NO POSTE QUE ESTA ESPECIFICADO NA TELEMETRIA ESCOLHIDA
#atualiza_json(c)
quebra_payload(a)
