import requests
from bs4 import BeautifulSoup as bs
import regex

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}


def get_google_links(page=0):
    if (page != 0):
        payload = {"q": "intitle:" + "{name}+{surname}".format(name=PROFILE['name'], surname=PROFILE['surname']),
                   "oq": "intitle:" + "{name}+{surname}".format(name=PROFILE['name'], surname=PROFILE['surname']),
                   "start": "{page}0".format(page=page)
                   }
    else:
        payload = {"q": "intitle:" + "{name}+{surname}".format(name=PROFILE['name'], surname=PROFILE['surname']),
                   "oq": "intitle:" + "{name}+{surname}".format(name=PROFILE['name'], surname=PROFILE['surname']),
                   }
    res = requests.get('https://www.google.com/search', headers=HEADERS, params=payload)
    soup = bs(res.text, "html.parser")
    items = soup.find_all('div', class_='g')
    links = []
    for item in items:
        links.append(item.find('a').get('href'))
    return links




name = "Виталий"
surname = "Смирнов"
PROFILE = {"name": name, "surname": surname}
result = []
page = 0
for i in range(2):
    result += get_google_links(page)
    page += 1
end = []
for item in result:


    if item == None:
        continue

    if(regex.match(r'^https', item)):
        end.append(item)
for i in range(10):
    print(end[i])


