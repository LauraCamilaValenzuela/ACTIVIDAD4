from pymongo.mongo_client import MongoClient #Se importa mongo para hacer la conexion

#CONEXIÓN
def conexion():      #se define la funcion llamada conexion
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"   #se define la URI a la que se conectara
    # Create a new client and connect to the server
    return MongoClient(uri)  #se retorna para poder ser utilizada 

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():    #se define una funcion que se llamara lectura de datos
    client = conexion() #se crea client en la que se llama a conexion para estar en mongo
    db = client.actividad4.data_real #se toma de la base de datos de la actividad 4 juto con la coleccion data real
    data_list = []  #se crea una lista
    for data_real_bd in db.find():   #en esta linea se hace un bucle que recorre toda data real
        data_list.append(data_real_bd) #se agrega los datos obetnidos a data list
    return data_list #se retornan los datos obtenidos de la base de datos

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""