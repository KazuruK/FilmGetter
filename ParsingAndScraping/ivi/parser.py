import requests
from ParsingAndScraping.ivi.scrapper import ivi_search
from ParsingAndScraping.assistants import big_num
from ParsingAndScraping.assistants import empty_string_cleaner
from bs4 import BeautifulSoup


def parse_this(film_name):
    url = ivi_search(film_name)
    if len(url) == 0:
        return []
    is_subscription_available = ''
    ivi_price = '399'
    hd_price = ''
    sd_price = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    free = str(soup.find('title'))
    if free.find('бесплатно') != -1:
        return ['Free']
    else:
        sub = soup.find('span', class_='nbl-button__secondaryText')
        if sub is not None:
            is_subscription_available = 'Available by Subscription. ' + ivi_price + ' rub'
    page = str(soup.find('video-info'))
    quote = big_num(page)
    if len(quote) > 1:
        del quote[len(quote) - 1]
        hd_price = str(quote[0])
        sd_price = str(quote[1])
    else:
        hd_price = str(quote[0])
    '''print(is_free) #for tests
    print(is_subscription_available)
    print(hd_price.strip())
    print(sd_price)'''
    output_list = [is_subscription_available, hd_price, sd_price]
    output = empty_string_cleaner(output_list)
    return output
