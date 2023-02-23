from influxdb import InfluxDBClient
import vars


client = InfluxDBClient(
    host=vars.influx_host, 
    port=vars.influx_port, 
    username=vars.influx_username, 
    password=vars.influx_password, 
    ssl=True, 
    verify_ssl=False)