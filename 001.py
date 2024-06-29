from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'html.parser')
title = bs.find('title')
print(title)
# print(bs.h1)