import requests

class KinopoiskAPIError(Exception):
    pass

class KinopoiskAPI:
    def __init__(self):
        self.key = '8fcf6015-6f7e-408c-9ced-d7c67167b5a2'
        self.domen = 'https://kinopoiskapiunofficial.tech'
        self.headersAPI = {
            'X-API-KEY': '8fcf6015-6f7e-408c-9ced-d7c67167b5a2'
        }

    def get_nameEn_by_keyword(self, text):
        url = self.domen + f'/api/v2.1/films/search-by-keyword?keyword={text}&page=1'
        request = requests.get(url, headers=self.headersAPI)
        return request.json()['films'][0]['nameEn']

    def get_by_id(self, id):
        url = self.domen + f'/api/v2.1/films/{id}/'
        request = requests.get(url, headers=self.headersAPI)
        if request.status_code != 200:
            raise KinopoiskAPIError(f'Запрос к фильму с id: {id},'
                                    f' вернул статус'
                                    f' {request.status_code}')
        return request.json()

    def get_film_url(self, id):
        url = self.domen + f'/api/v2.1/films/{id}/'
        request = requests.get(url, headers=self.headersAPI)
        return request.json()['data']['webUrl']

    def get_top_films(self):
        url = self.domen + f'/api/v2.2/films/top'
        request = requests.get(url, headers=self.headersAPI)
        return request.json()


def main():
    api = KinopoiskAPI()
    answer = api.get_nameEn_by_keyword("1+1")
    print(answer)


if __name__ == '__main__':
    main()
