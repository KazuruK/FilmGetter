import re
import requests
from bs4 import BeautifulSoup
from ParsingAndScraping.kinopoisk.kinopoiskAPI import KinopoiskAPI
from ParsingAndScraping.assistants import digits


def netflix_parcer(film_name):
    # prices = [599, 799, 999] '''Unused constant for price output'''
    string_getter = KinopoiskAPI()
    prepared_name = re.sub(" ", "-", str(string_getter.get_nameEn_by_keyword(film_name)))
    if len(prepared_name) == 0:
        return ['Not available on Netflix']
    url = 'https://www.flixwatch.co/movies/' + prepared_name
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    existence = str(soup.findAll("section", {"class": "error-404 not-found"}))
    if len(existence) > 4:
        tv_series_check = 'https://www.flixwatch.co/tvshows/' + prepared_name
        tv_page = requests.get(tv_series_check)
        bs = BeautifulSoup(tv_page.text, 'lxml')
        tv_existence = str(bs.findAll("section", {"class": "error-404 not-found"}))
        if len(tv_existence) > 4:
            return ['Not available on Netflix']
        else:
            return netflix_return_state(bs)
    else:
        return netflix_return_state(soup)


def netflix_return_state(soup):
    prices_url = 'https://help.netflix.com/ru/node/24926'
    plan = requests.get(prices_url)
    soupp = BeautifulSoup(plan.text, 'lxml')
    subs = soupp.findAll("strong")
    num_subs = digits(str(subs))
    values = str(soup.findAll("a", {"id": "Netflix"}))
    redirect = re.findall('https.+\d+', values)
    return [num_subs[0], num_subs[1], num_subs[2], redirect]
