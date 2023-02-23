from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address



from controllers.basicCRUD import basicCrud
from controllers.csvManipulation import csvManipulation
from controllers.influxSaveData import influx
from controllers.mongoDBCRUD import mongoDBCRUD


app = Flask(__name__)
CORS(app, support_credentials=True)



#LIMIT OF REQUESTS BY IP
limiter = Limiter(
    app, 
    key_func=get_remote_address, 
    default_limits=["200 per day", "60 per hour", "20 per minute"]
    #storage_uri="memcached://localhost:11211",    insert the path to save the logs
    #storage_options={}                            Default method it's not indicated for production
)


#BLUEPRINTS
app.register_blueprint(basicCrud)
app.register_blueprint(csvManipulation)
app.register_blueprint(influx)
app.register_blueprint(mongoDBCRUD)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')