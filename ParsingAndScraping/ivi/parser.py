import requests
from ParsingAndScraping.ivi.scrapper import ivi_search
from ParsingAndScraping.reg_parser import big_num
from bs4 import BeautifulSoup


def parse_this(film_name):
    film_id = str(ivi_search(film_name))
    url = 'https://www.ivi.ru/watch/' + film_id
    is_free = 0
    is_subscription_available = 0
    hd_price = ''
    sd_price = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    free = str(soup.find('title'))
    if free.find('бесплатно') != -1:
        is_free = 1
        is_subscription_available = 1
    else:
        sub = soup.find('span', class_='nbl-button__secondaryText')
        if sub is not None:
            is_subscription_available = 1
    page = str(soup.find('video-info'))
    quote = big_num(page)
    if len(quote) > 1:
        del quote[len(quote) - 1]
        hd_price = str(quote[0])
        sd_price = str(quote[1])
    else:
        hd_price = str(quote[0])
    print(is_free)
    print(is_subscription_available)
    print(hd_price.strip())
    print(sd_price)
    return is_free, is_subscription_available, sd_price, hd_price
