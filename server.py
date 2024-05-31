from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/")
async def data_caudal(request: Request):
  
  # Recibe los datos JSON de la solicitud
  datos_json = await request.json()

  # Muestra los datos en la consola
  print(json.dumps(datos_json, indent=4))

  # Devuelve una respuesta exitosa
  return {"message": "Datos recibidos correctamente"}