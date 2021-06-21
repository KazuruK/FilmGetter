from ParsingAndScraping.ivi.parser import parse_this


def main():
    film_name = input('Введите название фильма ')
    return parse_this(film_name)


if __name__ == '__main__':
    main()
