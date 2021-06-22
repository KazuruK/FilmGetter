import re


def big_num(page_info):
    num = re.findall("[0-9]{2,}", str(re.findall("{.*?}", page_info)))
    return num


def digits(data):
    digit = re.findall("\d+", data)
    return digit


def okko_templates(data):
    return re.sub('([\']url[\']:[\s].+[\']imageType[\']:[\s][\'][\w]{3,8}[\'].{3,3})', ' ', data)


def html_catcher(data):
    return
