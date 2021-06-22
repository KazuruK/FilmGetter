import re
import requests
from bs4 import BeautifulSoup


def scrap_megogo(film_name):
    url = 'https://megogo.ru/ru/search-extended?'
    params = {
        'q': film_name,
    }

    page = requests.get(url, params=params)
    soup = BeautifulSoup(page.text, 'lxml')
    film_info = str(soup.find("div", {"class": "thumb"}))
    url_get = str(re.findall('".+[.]html"', film_info))
    length = len(url_get)
    url = url_get[3:length - 3]
    return url
