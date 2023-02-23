from pymongo import MongoClient
import vars

try:
    mongoClient = MongoClient(vars.mongo_host_local, vars.mongo_port)
    mongoClient.server_info()
    db = mongoClient[vars.mongo_db]
except Exception as e:
    print(f'"Impossible to connect with MongoDB: "{e}')




########## VALIDATION SCHEMAS ###########

# db.createCollection("ConfigTags", { 
#         validator:{
#             $jsonSchema: {
#                 bsonType: "object",
# 				"additionalProperties": false,
#                 required: ["_id", "HOST", "DEVICE_NAME", "CONNECTION", "ROUTINE", "TAGS"],
#                 properties:{
# 					_id:{
#                         bsonType: "ObjectId",
#                         description: "Incorrect datatype"
#                     },
#                     HOST:{
#                         bsonType: "string",
#                         description: "Incorrect datatype"
#                     },
#                     DEVICE_NAME:{
#                         bsonType: "string",
#                         description: "Incorrect datatype"
#                     },
#                     CONNECTION:{
#                         bsonType: "string",
#                         description: "Incorrect datatype"
#                     },
#                     ROUTINE:{
#                         bsonType: "string",
#                         description: "Incorrect datatype"
#                     },
#                     TAGS:{
#                         bsonType: "Object",
#                         description: "Incorrect datatype"
#                     }
#                 }
#             }
#         }
# })