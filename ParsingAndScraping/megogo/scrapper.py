import re
import requests
from bs4 import BeautifulSoup
from ParsingAndScraping.assistants import substring_enter_count


def scrap_megogo(film_name):
    url = 'https://megogo.ru/ru/search-extended?'
    params = {
        'q': film_name,
    }

    page = requests.get(url, params=params)
    soup = BeautifulSoup(page.text, 'lxml')
    film_info = str(soup.find("div", {"class": "thumb"}))
    title = str(re.findall('title=["].+["]', film_info))
    current_string = str(re.findall('["].+["]', title))
    current_name = current_string[3:len(current_string) - 3]
    if substring_enter_count(film_name,current_name) == 0:
        return ['']
    url_get = str(re.findall('".+[.]html"', film_info))
    length = len(url_get)
    url = url_get[3:length - 3]
    return url
