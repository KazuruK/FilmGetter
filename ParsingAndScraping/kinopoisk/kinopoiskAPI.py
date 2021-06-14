import requests


class KinopoiskAPI:
    def __init__(self):
        self.key = '8fcf6015-6f7e-408c-9ced-d7c67167b5a2'
        self.domen = 'https://kinopoiskapiunofficial.tech'
        self.headersAPI = {
            'X-API-KEY': '8fcf6015-6f7e-408c-9ced-d7c67167b5a2'
        }

    def get_id_by_keyword(self, text):
        url = self.domen + f'/api/v2.1/films/search-by-keyword?keyword={text}&page=1'
        request = requests.get(url, headers=self.headersAPI)
        print(request.json())
        return request.json()['films'][1]['filmId']

    def get_by_id(self, id):
        url = self.domen + f'/api/v2.1/films/{id}/'
        request = requests.get(url, headers=self.headersAPI)
        return request.json()

    def get_film_url(self, id):
        url = self.domen + f'/api/v2.1/films/{id}/'
        request = requests.get(url, headers=self.headersAPI)
        return request.json()['data']['webUrl']


def main():
    api = KinopoiskAPI()
    answer = api.get_id_by_keyword('Начало')
    print(answer)

if __name__ == '__main__':
    main()