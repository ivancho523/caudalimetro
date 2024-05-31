import tweepy

# Ingresa tus credenciales de API de Twitter
consumer_key = "Kb3pAaHpcDG7qtWsBIqy6syYg"
consumer_secret = "SMGh1Xzjjxf57Nn6JkJGFyPPZri3DM4XinatGl46YFEklfOT3o"
access_token = "1793435649791414273-65CpVf8qWU2L8CPEk80miUNMYrd8pM"
access_token_secret = "6GLqfZxHw4LYh0iqYLAPfhRKg5JNHoQfDf9eBk6fAwPfs"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFm4twEAAAAAXhiNFki2IuVYoEPczUibGV3eyc8%3Dy2YhSC41h3Op9KhcPLpidYHdgYuMWZi2vzZlF0Vv78VI2EF8WM"

# V1 Autenticación Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Autenticación Twitter API
client = tweepy.Client(
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret,
    access_token=access_token, 
    access_token_secret=access_token_secret
)

# Carga de imagen al tweet
media_id = api.media_upload(filename="prueba.bmp").media_id_string
print(media_id)

# Texto que lleva el tweet
text = "Hola desde el server"

# Publicar tweet con texto e imagen
try:
    client.create_tweet(text=text, media_ids=[media_id])
    # client.create_tweet(text=text)
    print("Tweeted!")
except:
    print("no se pudo publicar, hay un error")

