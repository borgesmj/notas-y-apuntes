import requests, json

for i in range (10):
  results = requests.get("https://randomuser.me/api/")
  if results.status_code == 200:
    user = results.json()
    for person in user["results"]:
      # Creamos el nombre del archivo
      filename = f"""{person["name"]["first"]} {person["name"]["last"]}.jpg"""
      # Extraemos el archivo de la imagen
      picture = requests.get(person["picture"]["medium"])
      # creamos el nuevo archivo
      f = open(filename, "wb")
      f.write(picture.content)
      f.close()
      print(f"{filename} created")
