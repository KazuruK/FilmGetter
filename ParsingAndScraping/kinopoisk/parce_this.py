from requests_html import HTMLSession
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def parse_this(parsing_url, headers_without_useragent, bs_find_name, bs_find_class):

    url = parsing_url

    headers = headers_without_useragent
    headers['User-Agent'] = UserAgent().chrome

    session = HTMLSession()
    r = session.get(url, headers=headers)
    r.html.render()
    soup = BeautifulSoup(r.html.text, 'lxml')
    quote = soup.find(bs_find_name, class_=bs_find_class)
    print(soup)
    print(quote)
    with open('test.html', 'w', encoding='utf-8') as output_file:
        output_file.write(r.text)
