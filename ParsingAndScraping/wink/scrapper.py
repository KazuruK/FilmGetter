import requests
from ParsingAndScraping.assistants import big_num
from ParsingAndScraping.assistants import digits
from bs4 import BeautifulSoup


def wink_search(film_name):
    wink_search_pattern = "https://wink.rt.ru/search?query="
    pre_req = "%20".join(film_name.strip().split())
    request = wink_search_pattern + pre_req
    search_resp = requests.get(request)
    soup = BeautifulSoup(search_resp.text, 'lxml')
    page_info = str(soup.find("div", {"class": "item_i1j1p5p5"}))
    stringed_id = str(big_num(page_info))
    film_id = digits(stringed_id)
    return film_id[0]


def wink_film_url(film_name):
    film_id = wink_search(film_name)
    url = 'https://wink.rt.ru/media_items/' + film_id
    return url
