import requests
import re
from ParsingAndScraping.ivi.scrapper import ivisearch
from bs4 import BeautifulSoup

def parse_this(filmName):
    id = str(ivisearch(filmName))
    watchPattern = 'https://www.ivi.ru/watch/'
    url = watchPattern + id
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
    return (isFree, isSubscriptionAvailable, hdPrice, sdPrice)

