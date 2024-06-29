from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://m.huxiu.com/article/501984.html")
bs = BeautifulSoup(html.read(), "html.parser")

print(bs.get_text())