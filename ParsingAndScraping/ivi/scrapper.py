import requests
from ParsingAndScraping.reg_parser import digits


def ivi_search(film_name):
    url = 'https://api.ivi.ru/mobileapi/search/v5/'
    params = {
        'query': film_name,
        'fields': 'id,title',
        'app_version': '870'
    }
    page = requests.get(url, params=params)
    data = str(page.json())
    nums = digits(data)
    film_id = nums[0]
    return film_id
