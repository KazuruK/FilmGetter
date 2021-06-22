import re
import requests
from bs4 import BeautifulSoup
from ParsingAndScraping.kinopoisk.kinopoiskAPI import KinopoiskAPI


def netflix_parcer(film_name):
    prices = [599, 799, 999]
    prepared_name = re.sub(" ", "-", film_name)
    url = 'https://www.flixwatch.co/movies/' + prepared_name
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    existence = str(soup.findAll("section", {"class": "error-404 not-found"}))
    if len(existence) > 2:
        print('Not available on Netflix')
        return None
    else:
        values = str(soup.findAll("a", {"id": "Netflix"}))
        redirect = re.findall('https.+\d+', values)
        print(prices)
        return prices, redirect


def main():
    user_request = input("Введите название фильма ")
    string_getter = KinopoiskAPI()
    requested_string = str(string_getter.get_nameEn_by_keyword(user_request))
    netflix_parcer(requested_string)


if __name__ == '__main__':
    main()
