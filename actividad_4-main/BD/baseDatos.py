from pymongo.mongo_client import MongoClient

#CONEXIÓN
def conexion():
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri)

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():
    client = conexion()
    db = client.actividad4.data_real
    data_list = []
    for data_real_bd in db.find():
        data_list.append(data_real_bd)
    return data_list

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""