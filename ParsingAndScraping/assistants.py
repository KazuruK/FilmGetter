import re


def big_num(page_info):
    num = re.findall("[0-9]{2,}", str(re.findall("{.*?}", page_info)))
    return num


def digits(data):
    digit = re.findall("\d+", data)
    return digit


def empty_string_cleaner(input):
    while "" in input:
        input.remove("")
    return input


def substring_enter_count(input_name, current_name):
    if ':' in current_name or ':' in input_name:
        current_name = current_name.replace(':', '.')
        input_name = input_name.replace(':', '.')
    if 'ё' in current_name or 'ё' in input_name:
        current_name = current_name.replace('ё', 'е')
        input_name = input_name.replace('ё', 'е')
    if input_name[0:len(input_name) - 5].lower() in current_name.lower():
        return 1
    else:
        return 0
