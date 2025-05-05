import requests
import argparse


from bs4 import BeautifulSoup
from urllib.parse import urljoin

parser = argparse.ArgumentParser(description="Web scraping to check SEO for a griven URL")
parser.add_argument("url", type=str, help="The URL of the site you want to scrape and check")
args = parser.parse_args()
url = args.url

headers = {
    "User-agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("la peticion fue exitosa")

soup = BeautifulSoup(response.text, "html.parser")
print(f"Revisando la pagina: {url}")
    