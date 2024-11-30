
from CrearConexion import CrearConexion
from LeerConexion import LeerConexion
from ActualizarConexion import ActualizarConexion
from EliminarConexion import EliminarConexion


import mysql.connector
mydb = mysql.connector.connect (user="root", password= "12345", 
                                host= "localhost", database= "grafos",
                                auth_plugin="mysql_native_password")
Cursor = mydb.cursor()

def mostrarMenu():
    print("----------MENÚ-----------")
    print("| 1) Crear Conexión     |")
    print("| 2) Leer Conexión      |")
    print("| 3) Actualizar Conexión|")
    print("| 4) Eliminar Conexión  |")



def menu():
    while True:
        mostrarMenu()
        opcion = input("| Ingrese su opción: ")

        if opcion == "1":
            CrearConexion()
        elif opcion == "2":
            LeerConexion()
        elif opcion == "3":
            ActualizarConexion()
        elif opcion == "4":
            EliminarConexion()
        else:
            print("Opcion invalida, intente nuevamente")

if __name__ == "__main__":
    menu()