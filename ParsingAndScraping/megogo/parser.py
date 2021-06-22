import re

import requests
from ParsingAndScraping.megogo.scrapper import scrap_megogo
from ParsingAndScraping.reg_parser import digits
from bs4 import BeautifulSoup


def megogo_parser(film_name):
    is_free = 0
    is_subscription_available = 0
    url = scrap_megogo(film_name)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    values = soup.findAll("span", {"class": "pQualityItemPrice__value"})
    subscribe_button = str(soup.findAll("div", {"class": "btn-description"}))
    subscription = re.findall('Попробовать', subscribe_button)
    if (len(subscription) > 0) & (len(values) > 0):
        is_free = 1
        is_subscription_available = 1
    else:
        if len(subscription) > 0:
            is_subscription_available = 1
    prices = digits(str(values[0:2]))
    print(is_free)
    print(is_subscription_available)
    print(prices)
