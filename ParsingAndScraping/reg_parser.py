import re
def big_num(page_info):
    num = re.findall('[0-9]{2,}', str(re.findall('{.*?}', page_info)))
    return num

def digits(data):
    digit = re.findall('\d+', data)
    return digit