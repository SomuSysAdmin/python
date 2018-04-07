import requests
from bs4 import BeautifulSoup

session = requests.Session()
url = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
page = session.get(url).text

nobelList = BeautifulSoup(page, "html.parser")
anchorList = nobelList.findAll('a')

count=1
for anchor in anchorList:
    if 'href' in anchor.attrs:
        link = anchor['href']
        print(count, ":", link)
        count += 1
