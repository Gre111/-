from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# nameList = bs.findAll('span', {'class': 'green'})
nameList = bs.find(id='title')
print(nameList)
# for name in nameList:
    # print(name.get_text())