import socket
import json

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 80
    BUFFER_SIZE = 1024
    s.setblocking(False)  # Hacer el socket no bloqueante
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
            print(data)
            datos = data.decode('utf-8').replace("'", '"')
            print(datos)
            # Procesamiento de datos
            #...
            c.close()
        else:
            break  # Salir del bucle si no hay más datos
except OSError as e:
    print(f"Error al manejar la conexión: {e}")
finally:
    s.close()  # Asegúrate de cerrar el socket al final
