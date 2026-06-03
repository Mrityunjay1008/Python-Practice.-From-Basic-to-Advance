from bs4 import BeautifulSoup
import requests

source = requests.request("GET","https://example.com")

soup = BeautifulSoup(source.content, 'html.parser')

print(soup.prettify())

print()

print(soup.find("div",id="root"))