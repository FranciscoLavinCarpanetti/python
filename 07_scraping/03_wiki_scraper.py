from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

url = "https://es.wikipedia.org/wiki/Web_scraping"
headers = {
    "User-agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("la peticion fue exitosa")

    soup = BeautifulSoup(response.text, "html.parser")  

titulos =[titulo.string for titulo in soup.find_all("h1")]
print(titulos)


enlaces = [urljoin(url, enlace.get("href")) for enlace in soup.find_all("a")]
print(enlaces)


# recuperar todo el texto de la web

all_text = soup.get_text()
print(all_text)

main_text = soup.find("main").get_text()
print(main_text)


# recuperar ls imagenes

og_image = soup.find("meta", property="og:image")

if og_image:
    print(og_image["content"])
else:
    print("no se encontro imagen")   
