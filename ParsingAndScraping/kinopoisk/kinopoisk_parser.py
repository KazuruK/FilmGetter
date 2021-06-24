from ParsingAndScraping.kinopoisk import parce_this
from kinopoiskAPI import KinopoiskAPI


class KinopoiskParser(KinopoiskAPI):
    def __init__(self):
        super().__init__()

        self.headers = {
            'Accept-Language': 'ru',
            'Origin': 'https://yastatic.net',
            'Referer': 'https://yastatic.net/',
            'Access-Control-Allow-Origin': 'https://yastatic.net',
            'Content-Type': 'text/plain;charset=UTF-8'
        }
        self.bs_find_name = 'div'
        self.bs_find_class = 'styles_notActualText__1YDaG'

    def parse_film_price(self, film):
        id = self.get_id_by_keyword(film)
        url = self.get_film_url(id)
        parce_this.parse_this(url, self.headers, self.bs_find_name, self.bs_find_class)