import requests
import re

def ivisearch(filmName):

    url = 'https://api.ivi.ru/mobileapi/search/v5/'
    params = {
        'query': filmName,
        'fields': 'id,title',
        'app_version': '870'
    }
    page = requests.get(url, params=params)
    data = str(page.json())
    nums = re.findall('\d+', data)
    filmID = nums[0]
    return filmID