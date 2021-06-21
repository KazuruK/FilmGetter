import requests
import re
from ParsingAndScraping.reg_parser import big_num
from ParsingAndScraping.reg_parser import digits
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def winksearch(filmName):
    url = 'https://cnt-odcv-itv03.svc.iptv.rt.ru/api/v2/portal/group_search'
    '''urllogin = "some url of login page"
    payload = {'username': 'p05989', 'password': '123456'}
    with requests.session() as s:
        # fetch the login page
        s.get(url)
    r = s.post(url1, data=payload)

    filmName = input('Введите название фильма ')
    headers = {
        'session_id': '31e17481-d248-11eb-aac4-9c1d36dcd0f0:1951416:2237006:2',
        'query': filmName,
        'fields': 'name, id'
    }
    page = requests.get(url, params=headers)
    data = str(page.json())
    print(data)'''

    '''iviSearchPattern = "https://wink.rt.ru/search?query="
    preReq = "%20".join(filmName.strip().split())
    request = iviSearchPattern + preReq
    searchResp = requests.get(request)
    # responce = self.Response()
    #searchResp.html.render()
    # searchResp.json()
    soup = BeautifulSoup(searchResp.text, 'lxml')
    page_info = str(soup.find("div", {"class" : "item_i1j1p5p5"}))
    stringedID = str(big_num(page_info))
    filmID = digits(stringedID)
    print(filmID)
    return (filmID[0])
    #id = re.findall('[0-9]{2,}', str(re.findall('{.*?}', str(soup.find("div", {"class" : "item_i1j1p5p5"})))))
    #id = re.findall('[\d+]{4,}', filmInfo)
    #print(id[0])
    #print(request)'''

    url = 'https://cnt-odcv-itv03.svc.iptv.rt.ru/api/v2/portal/group_search'
    url_token = 'https://cnt-odcv-itv03.svc.iptv.rt.ru/api/v2/portal/session_tokens'

    params = {
        'query': 'Великий Гэтсби',  # сюда подставляйте название фильма для поиска
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
    filmName = '1917'
    winksearch(filmName)

if __name__ == '__main__':
    main()