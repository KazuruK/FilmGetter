from ParsingAndScraping.Netflix.parcer import netflix_parcer


def main():
    user_request = input("Введите название фильма ")
    print(netflix_parcer(user_request))
    netflix_parcer(user_request)


if __name__ == '__main__':
    main()
