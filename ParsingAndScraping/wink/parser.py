import re
import requests
from ParsingAndScraping.reg_parser import digits
from ParsingAndScraping.wink.scrapper import wink_search


def wink_parser(film_name):
    price_hd = ''
    price_uhd = ''
    free_available = 0
    sub_available = 0
    film_id = wink_search(film_name)
    url = 'https://sz-spbr-itv01.svc.iptv.rt.ru/api/v2/portal/media_items/' + film_id
    url_token = 'https://sz-spbr-itv01.svc.iptv.rt.ru/api/v2/portal/session_tokens'

    params = {
        'limit': 18,
    }
    token_page = requests.post(url_token, json={'fingerprint': ''})
    token = token_page.json()['session_id']
    headers = {
        'session_id': f'{token}'
    }

    result_page = requests.get(url, headers=headers, params=params)
    data = str(result_page.json())
    free_search = str(re.findall('[\']is_purchased[\'][:][\s]True', data))
    if len(free_search) > 2:
        free_available = 1
        sub_available = 1
    else:
        sub_search = str(re.findall('subscribe', data))
        if len(sub_search) > 2: sub_available = 1
    price_search = str(re.findall('навсегда за[\s][\d]+', data))
    prices = digits(price_search)
    lenght = len(prices)
    if lenght < 2:
        price_sd = prices[0]
    else:
        if lenght > 2:
            price_sd = prices[0]
            price_hd = prices[2]
            price_uhd = prices[1]
        else:
            price_sd = prices[0]
            price_hd = prices[1]

    print(free_available)
    print(sub_available)
    print(price_hd, price_sd, price_uhd)
    return free_available, sub_available, price_sd, price_hd, price_uhd
