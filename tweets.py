import tweepy
import pymongo
import matplotlib.pyplot as plt
import datetime

# Conexión a la base de datos MongoDB
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
base_datos = cliente["caudalimetro"]
coleccion = base_datos["rio_yi"]

# Obtener los datos de las últimas 24 horas
fecha_hora_actual = datetime.datetime.now()
fecha_hora_anterior = fecha_hora_actual - datetime.timedelta(days=1)

print(fecha_hora_anterior)
print(fecha_hora_actual)

datos = coleccion.find({"$and": [{"fecha": {"$gte": fecha_hora_anterior}}, {"fecha": {"$lt": fecha_hora_actual}}]})

# Extraer los valores de las variables
fechas = []
horas = []
niveles = []
velocidades = []
descargas = []

for dato in datos:
    fechas.append(dato["fecha"])
    horas.append(dato["hora"])
    niveles.append(dato["nivel"])
    velocidades.append(dato["velocidad"])
    descargas.append(dato["descarga"])

print(horas)
print(niveles)
print(velocidades)
print(descargas)

# Crear la gráfica
plt.figure(figsize=(10, 6))

plt.plot(horas, niveles, label="Nivel")
plt.plot(horas, velocidades, label="Velocidad")
plt.plot(horas, descargas, label="Descarga")

plt.xlabel("Hora")
plt.ylabel("Valor")
plt.title("Datos del Río Yi - Últimas 24 horas")

plt.legend()
plt.grid(True)

# Guardar la gráfica como imagen JPEG
carpeta_imagenes = "/home/caudalimetro/imagen"
nombre_imagen = "grafica_rio_yi.jpeg"

plt.savefig(f"{carpeta_imagenes}/{nombre_imagen}")

print(f"Gráfica guardada en: {carpeta_imagenes}/{nombre_imagen}")


# ########################################################################################################

# # Ingresa tus credenciales de API de Twitter
# consumer_key = "Kb3pAaHpcDG7qtWsBIqy6syYg"
# consumer_secret = "SMGh1Xzjjxf57Nn6JkJGFyPPZri3DM4XinatGl46YFEklfOT3o"
# access_token = "1793435649791414273-65CpVf8qWU2L8CPEk80miUNMYrd8pM"
# access_token_secret = "6GLqfZxHw4LYh0iqYLAPfhRKg5JNHoQfDf9eBk6fAwPfs"
# bearer_token = "AAAAAAAAAAAAAAAAAAAAAFm4twEAAAAAXhiNFki2IuVYoEPczUibGV3eyc8%3Dy2YhSC41h3Op9KhcPLpidYHdgYuMWZi2vzZlF0Vv78VI2EF8WM"

# # Autentificación en Twitter
# # V1 Twitter API Authentication
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)

# client = tweepy.Client(
#     consumer_key=consumer_key, 
#     consumer_secret=consumer_secret,
#     access_token=access_token, 
#     access_token_secret=access_token_secret
# )

# # Upload image to Twitter. Replace 'filename' your image filename.
# media_id = api.media_upload(filename="/home/caudalimetro/imagen/grafica_rio_yi.jpeg").media_id_string
# print(media_id)

# # Text to be Tweeted
# text = "Datos Monitoreo Río YI"

# # Send Tweet with Text and media ID
# client.create_tweet(text=text, media_ids=[media_id])
# print("Tweeted!")
