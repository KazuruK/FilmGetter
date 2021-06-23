from ParsingAndScraping.megogo.parser import megogo_parser


def main():
    film_name = input("Введите название фильма ")
    return megogo_parser(film_name)


if __name__ == "__main__":
    main()
