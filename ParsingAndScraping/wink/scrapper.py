import requests
from ParsingAndScraping.assistants import substring_enter_count


def wink_search(film_name):
    url = 'https://cnt-odcv-itv03.svc.iptv.rt.ru/api/v2/portal/group_search'
    url_token = 'https://cnt-odcv-itv03.svc.iptv.rt.ru/api/v2/portal/session_tokens'

    params = {
        'query': film_name,  # сюда подставляйте название фильма для поиска
        'limit': 18
    }
    token_page = requests.post(url_token, json={'fingerprint': ''})
    token = token_page.json()['session_id']
    headers = {
        'session_id': f'{token}'
    }

    result_page = requests.get(url, headers=headers, params=params)
    data = result_page.json()
    page_info = data['items'][0]['content_items'][00]
    if str(page_info['type']) == 'media_item':
        film_info = page_info['media_item']
        current_name = str(film_info['name'])
        if substring_enter_count(film_name, current_name) == 1:
            film_id = film_info['id']
            return str(film_id)
        else:
            return ''
    else:
        return ''


def wink_film_url(film_name):
    film_id = wink_search(film_name)
    if film_id == []:
        return []
    else:
        url = 'https://wink.rt.ru/media_items/' + film_id
        return url
