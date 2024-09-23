import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites'

r = requests.get(url)
r
soup = BeautifulSoup(r.content, 'lxml')

title = soup.find_all('h2',{'class':'site-heading'})
title
for t in title:
    print(t.getText())
