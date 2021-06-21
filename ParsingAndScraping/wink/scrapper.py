import requests
from ParsingAndScraping.reg_parser import big_num
from ParsingAndScraping.reg_parser import digits
from bs4 import BeautifulSoup


def wink_search(film_name):
    ivisearchpattern = "https://wink.rt.ru/search?query="
    pre_req = "%20".join(film_name.strip().split())
    request = ivisearchpattern + pre_req
    search_resp = requests.get(request)
    soup = BeautifulSoup(search_resp.text, 'lxml')
    page_info = str(soup.find("div", {"class": "item_i1j1p5p5"}))
    stringed_id = str(big_num(page_info))
    film_id = digits(stringed_id)
    return film_id[0]
