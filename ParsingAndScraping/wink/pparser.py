import requests

def pparse():
    url = 'https://sz-spbr-itv01.svc.iptv.rt.ru/api/v2/portal/media_items/54983465'
    url_token = 'https://sz-spbr-itv01.svc.iptv.rt.ru/api/v2/portal/session_tokens'

    params = {
        'query': 'Великий',  # сюда подставляйте название фильма для поиска
        'limit': 18
    }
    token_page = requests.post(url_token, json={'fingerprint': ''})
    token = token_page.json()['session_id']
    headers = {
        'session_id': f'{token}'
    }

    result_page = requests.get(url, headers=headers, params=params)
    data = result_page.json()
    print(data)

def main():
    pparse()

if __name__ == '__main__':
    main()