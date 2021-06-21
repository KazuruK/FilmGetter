import requests
from bs4 import BeautifulSoup
from ParsingAndScraping.wink.scrapper import winksearch
from ParsingAndScraping.reg_parser import digits
from requests_html import HTMLSession
import re
def wink_parser():
    session = HTMLSession()
    filmName = input('Введите название фильма ')
    id = winksearch(filmName)
    url = 'https://wink.rt.ru/media_items/' + id + '/payments'
    #url = watchPattern + id
    isFree = 0
    isSubscriptionAvailable = 0
    hdPrice = ''
    sdPrice = ''
    response = session.get(url)
    response.html.render()
    soup = BeautifulSoup(response.text, 'lxml')
    #    hd_info = str(soup.findAll("span", {"data-test" : "purchase-option-price"}))
    hd_info = str(soup.findAll('249'))
    #hdd_info = hd_info.find('amount')
    hdPrice = str(re.findall('[\W][\d]+', hd_info))
    hdwe = digits(hdPrice)
    print(hdwe)
    print(hd_info)
    #print(hdd_info)
    #print(hdPrice[len(hdPrice)-1])
    with open('test.html', 'w', encoding='utf-8') as output_file:
        output_file.write(soup.text)


def main():
    wink_parser()

if __name__ == '__main__':
    main()