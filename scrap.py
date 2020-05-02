import requests
from bs4 import BeautifulSoup
import csv

url = 'https://web.archive.org/web/20121010200620/http://www.nga.gov/collection/anR7.htm'
page = requests.get(url) 
soup = BeautifulSoup(page.text, 'html.parser') 
#acessando a url e extraindo o site em um BS object

document = open('SiteHTML.html', 'w') #vai sobrescrever o arquivo anterior
document.write(soup.prettify())

link_anterior = soup.find(class_='AlphaNav')
link_anterior.decompose()

lista_nomes = soup.find(class_= 'BodyText')
lista_nomes_itens = lista_nomes.find_all('a')

for artista_nome in lista_nomes_itens:
    nomes = artista_nome.contents[0]
    links = 'https://web.archive.org' + artista_nome.get('href')
    print(nomes)
    print(links)









