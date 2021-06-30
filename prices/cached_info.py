from functools import wraps
import datetime as dt
import json
import time
from ParsingAndScraping.ivi import parser as parser_ivi
from ParsingAndScraping.megogo import parser as parser_megogo
from ParsingAndScraping.Netflix import parcer as parser_netflix
from ParsingAndScraping.wink import parser as parser_wink


def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции {func.__name__}: {execution_time} с.')
        return result

    return wrapper


@time_check
def parse_ivi(film_name):
    return parser_ivi.parse_this(film_name)


@time_check
def parse_megogo(film_name):
    return parser_megogo.megogo_parser(film_name)


@time_check
def parse_netflix(film_name):
    return parser_netflix.netflix_parcer(film_name)


@time_check
def parse_wink(film_name):
    return parser_wink.wink_parser(film_name)


def parse_all(film_name):
    price_dict = {"ivi": parse_ivi(film_name),
                  "megogo": parse_megogo(film_name),
                  "netflix": parse_netflix(film_name),
                  "wink": parse_wink(film_name)}
    price_json = json.dumps(price_dict, sort_keys=True, indent=4)
    price_json = json.loads(price_json)
    return price_json


def main():
    parse_all("Начало")
    parse_all("Начало")


if __name__ == '__main__':
    main()
