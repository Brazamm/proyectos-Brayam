import mysql.connector
mydb = mysql.connector.connect (user="root", password= "12345", 
                                host= "localhost", database= "grafos",
                                auth_plugin="mysql_native_password")
Cursor = mydb.cursor()

def EliminarConexion(IdConexion):
    Cursor.callproc("EliminarConexion",(IdConexion,))
    for result in Cursor.stored_results():
        print(result.fetchall())
    mydb.commit()

#frontend
p_id_conexion = input ("ingrese el id de la conexion a eliminar: ")
EliminarConexion (p_id_conexion)