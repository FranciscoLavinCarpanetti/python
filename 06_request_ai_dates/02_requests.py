###
# como hacer peticiones a API a Python
# con y sin dependencias

# sin dependencias (dificil y demasiado largo)
import urllib.request
import json

api_post = 'https://jsonplaceholder.typicode.com/posts'

try:
    response = urllib.request.urlopen(api_post)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
except urllib.error.HTTPError as e:
    print(f"Error en la petición: {e}")





