import requests
from bs4 import BeautifulSoup
import csv

lista = csv.writer(open('Artistas2.csv', 'w'))
lista.writerow(['Nome','Link'])

for i in range(26):
    url = 'https://web.archive.org/web/20121010200620/http://www.nga.gov/collection/anL' + str(i+1)+'.htm'
    page = requests.get(url) 
    soup = BeautifulSoup(page.text, 'html.parser') 
    #acessando a url e extraindo o site em um BS object

    link_anterior = soup.find(class_='AlphaNav')
    link_anterior.decompose()

    lista_nomes = soup.find(class_= 'BodyText')
    lista_nomes_itens = lista_nomes.find_all('a')

    for artista_nome in lista_nomes_itens:
        nomes = artista_nome.contents[0]
        links = 'https://web.archive.org' + artista_nome.get('href')
        lista.writerow([nomes, links])









