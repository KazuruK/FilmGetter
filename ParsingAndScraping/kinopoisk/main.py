from ParsingAndScraping.kinopoisk.kinopoisk_parser import KinopoiskParser


def main():
    parser = KinopoiskParser()
    parser.parse_film_price('Начало')


if __name__ == '__main__':
    main()
