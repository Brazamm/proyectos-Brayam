import mysql.connector
mydb = mysql.connector.connect (user="root", password= "12345", 
                                host= "localhost", database= "grafos",
                                auth_plugin="mysql_native_password")
Cursor = mydb.cursor()

def CrearConexion(IdOrigen, IdDestino):
    Cursor.callproc("CrearConexion",(IdOrigen, IdDestino,))
    for result in Cursor.stored_results():
        print(result.fetchall())
    mydb.commit()

#frontend
p_origen_id = input ("ingrese el nodo de origen: ")

p_destino_id = input ("ingrese el nodo de destino: ")
CrearConexion (p_origen_id, p_destino_id)