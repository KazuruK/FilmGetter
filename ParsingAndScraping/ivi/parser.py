import requests
import re
import scrapper
from bs4 import BeautifulSoup

def parse_this():

    url = 'https://www.ivi.ru/watch/109916'
    isFree = 0
    isSubscriptionAvailable = 0
    hdPrice = ''
    sdPrice = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    free = str(soup.find('title'))
    if (free.find('бесплатно') != -1) :
        isFree = 1
        isSubscriptionAvailable = 1
    else :
        sub = soup.find('span', class_ = 'nbl-button__secondaryText')
        if (sub != None) : isSubscriptionAvailable = 1
    quotes = str(soup.find('video-info'))
    #test = str(re.findall('{.*?}', quote))
    quote = re.findall('[0-9]{2,}', str(re.findall('{.*?}', str(soup.find('video-info')))))
    if (len(quote)>1):
        del quote[len(quote)-1]
        hdPrice = str(quote[0])
        sdPrice = str(quote[1])
    else:
        hdPrice = str(quote[0])
    print(isFree)
    print(isSubscriptionAvailable)
    print(hdPrice.strip())
    print(sdPrice)
    #with open('test.html', 'w', encoding='utf-8') as output_file:
        #output_file.write(response.text)

def main():
    parse_this()

if __name__ == '__main__':
    main()