import os
import vars
from flask_mail import Message
from models.mongodb import db





def send_email(token, useremail):
    try:
        real_path = '/'.join(os.path.realpath(__file__).split("/")[:-1])
        with open(f"./recover_password.html", encoding="utf-8") as file:
            html = file.read()
        html = html.replace("$(TOKEN)", str(token))
        html = html.replace("$(TIME_TO_EXPIRED)",
                            str(vars.token_expired_minutes))
        msg = Message('RECOVERY TOKEN - Do not answer', 
                        sender=vars.mail_username,
                        recipients=[useremail],
                        html=html
                      )
        vars.mail.send(msg)
        return True
    except Exception as e:
        return False, str(e)



######################### MONGODB ##################################
def insertMongoDB(collection, document, type):
    try:
        selectedCollection = db[collection]
        if type == 1:
            selectedCollection.insert_one(document)
        elif type == 2:
            selectedCollection.insert_many(document)
        else:
            pass
    except Exception as e:
        print('Except: Impossible to save in MongoDB', f"Error: {e}")

def deleteDocumentsFromMongo(collection, condition):
    try:
        selectedCollection = db[collection]
        result = selectedCollection.delete_many(condition)
        return {'FL_STATUS': True, 'message':f"{result.deleted_count} documents deleted."}
    except Exception as e:
        print('Except: Impossible to delete documents from MongoDB', f"Error: {e}")