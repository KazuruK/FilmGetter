import requests
from ParsingAndScraping.assistants import digits
from ParsingAndScraping.assistants import substring_enter_count


def ivi_search(film_name):
    url = 'https://api.ivi.ru/mobileapi/search/v5/'
    params = {
        'query': film_name,
        'fields': 'id,title',
        'app_version': '870'
    }
    page = requests.get(url, params=params)
    data = page.json()
    length = data['result']
    if not length:
        return []
    current_name = data['result'][0]['title']
    nums = digits(str(data))
    if len(nums) == 0 | substring_enter_count(film_name, current_name) == 0:
        return []
    else:
        film_id = nums[0]
        url = 'https://www.ivi.ru/watch/' + str(film_id)
        return url
