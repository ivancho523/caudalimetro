import socket
import json
import datetime
from pymongo import MongoClient

# Replace with your MongoDB connection details
client = MongoClient("mongodb://localhost:27017/")  # Adjust host and port if needed
db = client["caudalimetro"]
collection = db["rio_yi"]


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8000
    BUFFER_SIZE = 1024
#    s.setblocking(False)  # Hacer el socket no bloqueante
    s.bind(('localhost', port))  # Asegúrate de que esta IP y puerto son correctos
    s.listen(5)
    print("Conexión creada")

except OSError as e:
    print(f"Error al iniciar el servidor: {e}")

try:
    while True:
        c, addr = s.accept()
        print("Conexión externa de: ", addr)
        data = c.recv(BUFFER_SIZE)
        if data:
            print(type(data))
            print("------------DATOS BRUTOS---------------")
            print(data)
            datos = data.decode('utf-8').replace("'", '"')
            print("------------DATOS PROCESADOS-----------")
            print(datos)
            # Procesamiento de datos
            # Guardar datos procesados en un archivo .txt
            #fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            #nombre_archivo = f"datos_procesados_{fecha_hora}.txt"
            #with open(nombre_archivo, 'w') as archivo:
            #    archivo.write(datos)
            respuesta = "HTTP/1.1 200 OK\r\n\r\n".encode('utf-8')
            c.sendall(respuesta)
            c.close()
            #    
            file_datos = open("/home/caudalimetro/datos_caudal.txt", "a+")
            file_datos.write(datos)
            file_datos.close()
            #...
            datos_nuevos = data.decode('utf-8')
            # Dividir la trama por líneas
            lineas = datos_nuevos.splitlines()
            print ("########## estas son las líneas########")
            print (lineas)
            # Procesar datos por línea
            for linea in lineas[12:]:  # Empezar desde la línea 13 (D;...)
                if linea.startswith("D;"):
                    # Separar valores por punto y coma
                    valores = linea.split(";")
                    # Extraer datos de interés
                    fecha = valores[1].split(" ")[0]  # Extraer solo la fecha
                    hora = valores[1].split(" ")[1] # Extraer solo la hora
                    # nivel = float(valores[3].split(",")[0])
                    nivel = valores[2]
                    velocidad = valores[3]
                    descarga = valores[5]  # Eliminar símbolo de unidad
                    # Crear documento para MongoDB
                    documento = {
                        "fecha": fecha,
                        "hora": hora,
                        "nivel": nivel,
                        "velocidad": velocidad,
                        "descarga": descarga
                    }
                    print(documento)
                    # file_datos_exactos = open("/home/caudalimetro/valores_exactos.txt", "a+")
                    # file_datos_exactos.write(str(documento))
                    # file_datos_exactos.close()
                    # Insertar documento en la colección
                    insertar = collection.insert_one(documento)
                    print(f"ID del dato: {insertar.inserted_id}")
                    print("Datos almacenados en la colección rio_yi.")
            # Cerrar conexión
            client.close()
            
        else:
            break  # Salir del bucle si no hay más datos
except OSError as e:
    print(f"Error al manejar la conexión: {e}")
finally:
    s.close()  # Asegúrate de cerrar el socket al final
