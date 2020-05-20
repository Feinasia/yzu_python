import requests
from bs4 import BeautifulSoup

url  = 'https://tw.stock.yahoo.com/q/bc?s=2330'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')


print(html)