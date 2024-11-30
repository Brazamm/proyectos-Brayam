import mysql.connector

# Configuración de la conexión a MySQL
def obtener_conexion():
    return mysql.connector.connect(
        user="root",
        password="12345",
        host="localhost",
        database="grafos",
        auth_plugin="mysql_native_password"
    )
def CrearConexion(IdOrigen, IdDestino):
    mydb = obtener_conexion()
    cursor = mydb.cursor()
    cursor.callproc("CrearConexion", (IdOrigen, IdDestino,))
    for result in cursor.stored_results():
        print(result.fetchall())
    mydb.commit()
    mydb.close()


def LeerConexion(IdCiudad):
    mydb = obtener_conexion()
    cursor = mydb.cursor()
    cursor.callproc("LeerConexion", (IdCiudad,))
    for result in cursor.stored_results():
        print(result.fetchall())
    mydb.close()


def ActualizarConexion(IdConexion, IdOrigen, IdDestino):
    mydb = obtener_conexion()
    cursor = mydb.cursor()
    cursor.callproc("ActualizarConexion", (IdConexion, IdOrigen, IdDestino,))
    for result in cursor.stored_results():
        print(result.fetchall())
    mydb.commit()
    mydb.close()


def EliminarConexion(IdConexion):
    mydb = obtener_conexion()
    cursor = mydb.cursor()
    cursor.callproc("EliminarConexion", (IdConexion,))
    for result in cursor.stored_results():
        print(result.fetchall())
    mydb.commit()
    mydb.close()

def mostrar_menu():
    print("----------MENÚ-----------")
    print("| 1) Crear Conexión     |")
    print("| 2) Leer Conexión      |")
    print("| 3) Actualizar Conexión|")
    print("| 4) Eliminar Conexión  |")
    print("| 5) Salir              |")
    print("-------------------------")

def menu():
    while True:
        mostrar_menu()
        opcion = input("| Ingrese su opción: ")

        if opcion == "1":
            # Solicitar datos para Crear Conexión
            p_origen_id = input("Ingrese el nodo de origen: ")
            p_destino_id = input("Ingrese el nodo de destino: ")
            CrearConexion(p_origen_id, p_destino_id)

        elif opcion == "2":
            # Solicitar datos para Leer Conexión
            p_id_nodo = input("Ingrese el nodo de la ciudad a consultar: ")
            LeerConexion(p_id_nodo)

        elif opcion == "3":
            # Solicitar datos para Actualizar Conexión
            p_id_conexion = input("Ingrese el ID de la conexión: ")
            p_origen_id = input("Ingrese el nodo de origen: ")
            p_destino_id = input("Ingrese el nodo de destino: ")
            ActualizarConexion(p_id_conexion, p_origen_id, p_destino_id)

        elif opcion == "4":
            # Solicitar datos para Eliminar Conexión
            p_id_conexion = input("Ingrese el ID de la conexión a eliminar: ")
            EliminarConexion(p_id_conexion)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()
