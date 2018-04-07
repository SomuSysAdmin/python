import requests
from bs4 import BeautifulSoup

session = requests.Session()
url = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
page = session.get(url).text

nobelList = BeautifulSoup(page, "html.parser")

# Print the birthdays of all the nobel laureates

trows = nobelList.find('table', {'class' : ["wikitable", "sortable"]}).findAll('tr')
laurs = []
for r in trows:
    for candidate in r.find_all('span', {'class': "vcard"}):
        laurs.append(candidate.a)

for l in laurs:
    print("Name: %s" % l.contents[0])
    link = "https://en.wikipedia.org" + l['href']
    pg2 = session.get(link).text

    pg2soup = BeautifulSoup(pg2, 'html.parser')
    info = pg2soup.find('table', {'class' : ['infobox', 'biography', 'vcard']}).find_all('tr')
    for r in info:
        bday = r.find('span', {'class': "bday"})
        if bday is not None:
            bday = bday.contents[0]
            break
    print("Birthday:",bday, "\n")