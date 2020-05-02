import requests
from bs4 import BeautifulSoup
import csv

url = 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm'
page = requests.get(url) 
soup = BeautifulSoup(page.text, 'html.parser') 
#acessando a url e extraindo o site em um BS object

document = open('SiteHTML.txt', 'w') #vai sobrescrever o arquivo anterior
document.write(soup.prettify())






