import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')