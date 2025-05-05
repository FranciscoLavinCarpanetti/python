import requests
import re

url = "https://www.apple.com/es/shop/buy-mac/macbook-pro"


response = requests.get(url)

if response.status_code == 200:
    print("La peticion fue exitosa")
html = response.text

price_pattern = r'<span class=rc-prices-fullprice">(.*?)</span>'

match = re.search(price_pattern, html)

if match:
    print(f"El precio es: {match.group(0)}")
    