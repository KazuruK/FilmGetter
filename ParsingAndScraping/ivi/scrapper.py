import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def ivisearch():
    session = HTMLSession()
    iviSearchPattern = "http://ivi.ru/search/?ivi_search="
    userRequest = input('Введите название фильма ')
    preReq = "%20".join(userRequest.strip().split())
    request = iviSearchPattern + preReq
    searchResp = session.get(request)
    #responce = self.Response()
    searchResp.html.render()
    #searchResp.json()
    soup = BeautifulSoup(searchResp.text, 'lxml')
    with open('test.html', 'w', encoding='utf-8') as output_file:
        output_file.write(searchResp.text)
    print(request)


def main():
    ivisearch()

if __name__ == '__main__':
    main()