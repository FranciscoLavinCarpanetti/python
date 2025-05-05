from bs4 import BeautifulSoup
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-pro/16-pulgadas"

response = requests.get(url)

if response.status_code == 200:
 print("La peticion fue existosa")

 soup = BeautifulSoup(response.text, "html.parser")

 #print(soup.prettify())
 title_tag = soup.title
 if title_tag:
     print(f"El titulo de la pagina es:  {title_tag.string}")

 metas = soup.title.parent.find_all("meta")
 print(f"El numero de meta tags es: {len(metas)}")   

 price_span = soup.find("span", class_="rc-prices-fullprice")
 if price_span:
     print(f"El precio del producto es: {price_span.text}")

# todos los precios
pricess_span = soup.find_all("span", class_="rc-prices-fullprice")
for price in pricess_span:
   print(f"El precio de cada articulo es: {price.text}")     


products = soup.find_all (class_="rc-productselection-item")
for product in products:
   name = product.find(class_="list-title").text
   price = product.find(class_="rc-prices-fullprice").text
print(f"El producto con las caracteristicas:\n{name}\n precio de {price}")
