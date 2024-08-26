import requests, json, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


def fetchTracks(year):
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    clientID = os.getenv('CLIENT_ID')
    clientSecret = os.getenv('CLIENT_SECRET')
    # Realizamos el login a la app
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(clientID, clientSecret)

    response = requests.post(url, data=data, auth=auth)

    token = response.json()["access_token"]

    # con el token hecho, procedemos a hacer una consulta
    url = "https://api.spotify.com/v1/search?"
    search = f"q=year%3A{year}&type=track&limit=10&offset=0"
    headers = {"Authorization": f"Bearer {token}"}

    # realizamos la busqueda
    fullUrl = f"{url}{search}"
    response = requests.get(fullUrl, headers=headers)

    data = response.json()
    
    songsList = ''
    for track in data["tracks"]["items"]:
        songName = track["name"]
        artistName = track["artists"][0]["name"]
        previewUrl = track["preview_url"]
        if previewUrl is None:
            continue
        else:
            f = open("src/songTemplate.html", "r")
            template = f.read()
            f.close()
            template = template.replace("{songName}", songName)
            template = template.replace("{artist}", artistName)
            template = template.replace("{url}", previewUrl)
            songsList += template

    return songsList
        
        



