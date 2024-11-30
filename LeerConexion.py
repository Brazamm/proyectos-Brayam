import mysql.connector
mydb = mysql.connector.connect (user="root", password= "12345", 
                                host= "localhost", database= "grafos",
                                auth_plugin="mysql_native_password")
Cursor = mydb.cursor()

def LeerConexion(IdCiudad):
    Cursor.callproc("LeerConexion",(IdCiudad,))
    for result in Cursor.stored_results():
        print(result.fetchall())
    mydb.commit()

#frontend
p_id_nodo = input ("ingrese el nodo de la ciudad a a consultar: ")
LeerConexion (p_id_nodo)