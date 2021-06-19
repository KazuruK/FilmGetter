from ParsingAndScraping.ivi.parser import parse_this

def main():
    filmName = input('Введите название фильма ')
    return parse_this(filmName)

if __name__ == '__main__':
    main()