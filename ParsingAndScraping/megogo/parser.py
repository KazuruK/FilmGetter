import re

import requests
from ParsingAndScraping.megogo.scrapper import scrap_megogo
from ParsingAndScraping.reg_parser import digits
from bs4 import BeautifulSoup


def megogo_parser(film_name):
    url = scrap_megogo(film_name)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    values = str(soup.findAll("span", {"class": "pQualityItemPrice__value"}))
    subscribe_button = str(soup.findAll("div", {"class": "btn-description"}))
    subscription = re.findall('Попробовать', subscribe_button)
    if (len(subscription) < 3) & (len(values) < 3):
        print('ahkfdawjldaf;lbgfkdjbsf.')
    prices = digits(values)
    asd = str(soup)
    '''print(asd)
    print(subscription)'''
    print(prices)


def main():
    megogo_parser()


if __name__ == "__main__":
    main()
