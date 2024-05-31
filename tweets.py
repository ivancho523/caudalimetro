import tweepy

# Ingresa tus credenciales de API de Twitter
consumer_key = "Kb3pAaHpcDG7qtWsBIqy6syYg"
consumer_secret = "SMGh1Xzjjxf57Nn6JkJGFyPPZri3DM4XinatGl46YFEklfOT3o"
access_token = "1793435649791414273-65CpVf8qWU2L8CPEk80miUNMYrd8pM"
access_token_secret = "6GLqfZxHw4LYh0iqYLAPfhRKg5JNHoQfDf9eBk6fAwPfs"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFm4twEAAAAAXhiNFki2IuVYoEPczUibGV3eyc8%3Dy2YhSC41h3Op9KhcPLpidYHdgYuMWZi2vzZlF0Vv78VI2EF8WM"

# Autentificación en Twitter
# V1 Twitter API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# # V2 Twitter API Authentication
# client = tweepy.Client(
#     bearer_token,
#     consumer_key,
#     consumer_secret,
#     access_token,
#     access_token_secret,
#     wait_on_rate_limit=True,
# )

client = tweepy.Client(
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret,
    access_token=access_token, 
    access_token_secret=access_token_secret
)

# Upload image to Twitter. Replace 'filename' your image filename.
media_id = api.media_upload(filename="prueba.bmp").media_id_string
print(media_id)

# Text to be Tweeted
text = "Hello Twitter!"

# Send Tweet with Text and media ID
client.create_tweet(text=text, media_ids=[media_id])
print("Tweeted!")
# # Mensaje del tweet
# mensaje = "Este es un tweet publicado desde Python!"

# # Publica el tweet
# try:
#     api.update_status(status=mensaje)
#     print("Tweet publicado con éxito!")
# except:
#     print("Error al publicar tweet")
