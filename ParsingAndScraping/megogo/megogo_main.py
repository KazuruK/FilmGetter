from ParsingAndScraping.megogo.parser import megogo_parser


def main():
    film_name = "Алиса в стране чудес"
    print(megogo_parser(film_name))
    return megogo_parser(film_name)


if __name__ == "__main__":
    main()
