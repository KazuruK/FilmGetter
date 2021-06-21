from ParsingAndScraping.wink.parser import wink_parser


def main():
    film_name = input("Введите название фильма ")
    return wink_parser(film_name)


if __name__ == "__main__":
    main()
