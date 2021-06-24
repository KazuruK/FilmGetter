from functools import wraps
import datetime as dt
import json
import time
from ParsingAndScraping.ivi import parser as parser_ivi
from ParsingAndScraping.megogo import parser as parser_megogo
from ParsingAndScraping.Netflix import parcer as parser_netflix
from ParsingAndScraping.wink import parser as parser_wink

cache = {}


def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции {func.__name__}: {execution_time} с.')
        return result

    return wrapper


def cache_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = str(args) + func.__name__
        if not cache_key in cache or (cache[cache_key][1] - dt.datetime.today()).days <= -3:
            result = func(*args, **kwargs)
            cache[cache_key] = [result, dt.datetime.today()]
            return result
        return cache[cache_key][0]

    return wrapper

@time_check
@cache_this
def parse_ivi(film_name):
    return parser_ivi.parse_this(film_name)

@time_check
@cache_this
def parse_megogo(film_name):
    return parser_megogo.megogo_parser(film_name)

@time_check
@cache_this
def parse_netflix(film_name):
    return parser_netflix.netflix_parcer(film_name)

@time_check
@cache_this
def parse_wink(film_name):
    return parser_wink.wink_parser(film_name)


def parse_all(film_name):
    price_dict = {"film_name": film_name,
                  "ivi": parse_ivi(film_name),
                  "megogo": parse_megogo(film_name),
                  "netflix": parse_netflix(film_name),
                  "wink": parse_wink(film_name)}
    print(price_dict)
    price_json = json.dumps(price_dict, sort_keys=True, indent=4)
    print("а тут json:")
    print(price_json)
    return price_json


def main():
    parse_all("Начало")
    parse_all("Начало")



if __name__ == '__main__':
    main()