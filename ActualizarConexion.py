import mysql.connector
mydb = mysql.connector.connect (user="root", password= "12345", 
                                host= "localhost", database= "grafos",
                                auth_plugin="mysql_native_password")
Cursor = mydb.cursor()

def ActualizarConexion(IdConexion, IdOrigen, IdDestino ):
    Cursor.callproc("ActualizarConexion",(IdConexion, IdOrigen, IdDestino,))
    for result in Cursor.stored_results():
        print(result.fetchall())
    mydb.commit()

#frontend
p_id_conexion = input ("ingrese el id de la conexion: ")
p_origen_id = input ("Ingrese el nodo del origen: ")
p_destino_id = input ("Ingrese el nodo del destino: ")

ActualizarConexion (p_id_conexion, p_origen_id, p_destino_id)