import re
import requests
from ParsingAndScraping.megogo.scrapper import scrap_megogo
from ParsingAndScraping.assistants import digits
from ParsingAndScraping.assistants import empty_string_cleaner
from bs4 import BeautifulSoup


def megogo_parser(film_name):
    subscription_price = '397'
    hd_price = ''
    sd_price = ''
    url = scrap_megogo(film_name)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    values = soup.findAll("span", {"class": "pQualityItemPrice__value"})
    subscribe_button = str(soup.findAll("div", {"class": "btn-description"}))
    subscription = re.findall('Попробовать', subscribe_button)
    if (len(subscription) == 0) & (len(values) == 0):
        return ['Free']
    else:
        if len(subscription) > 0:
            return ['Available by subscription ' + subscription_price + ' rub']
    prices = digits(str(values[0:2]))
    if len(prices) == 2:
        hd_price = prices[0]
        sd_price = prices[1]
    else:
        hd_price = prices[0]
    '''print(is_free)   #for tests
    print(is_subscription_available)
    print(prices[0])
    print(prices[1])'''
    output_list = [hd_price, sd_price]
    output = empty_string_cleaner(output_list)
    return output
