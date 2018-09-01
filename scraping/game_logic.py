import requests
from random import choice
from types import SimpleNamespace
from csv import DictReader
from bs4 import BeautifulSoup

BASE_URL = 'http://quotes.toscrape.com'


def read_quotes(filename):
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def play_game(quotes):

    # game-round data
    quote_dict = choice(quotes)
    quote = SimpleNamespace(**quote_dict)
    remaining_guesses = 4
    guess = ''

    print("\nHere's a quote:\n")
    print(quote.text)
    while guess.lower() != quote.author.lower() and remaining_guesses > 0:
        # print(quote.author)
        guess = input('\nWho said this quote? '
                      f'Guesses remaining: {remaining_guesses}\n'
                      ': ')
        if guess.lower() == quote.author.lower():
            print('you win!')
        else:
            remaining_guesses -= 1
            if remaining_guesses is 3:
                res = requests.get(f'{BASE_URL}{quote.bio_link}')
                soup = BeautifulSoup(res.text, 'html.parser')
                birth_date = soup.find(
                    class_='author-born-date').get_text()
                birth_place = soup.find(
                    class_='author-born-location').get_text()
                print('\nFirst hint: The author was born on '
                      f'{birth_date} in {birth_place}')
            elif remaining_guesses is 2:
                print('Second hint: The author\'s '
                      f'first name starts with "{quote.author[0]}"')
            elif remaining_guesses is 1:
                last_initial = quote.author.split(' ')[1][0]
                print('Last hint: The author\'s '
                      f'last name starts with "{last_initial}"')
            else:
                print('Sorry you ran out of guesses. '
                      f'The answer was {quote.author}')

    again = ''
    while again not in ('y', 'yes', 'n', 'no'):
        again = input('Would you like to play again? [y/n]')
    if again.lower() in ('yes', 'y'):
        return play_game()
    else:
        print('Thanks for playing!')


# Game Init
quotes = read_quotes('quotes.csv')
play_game(quotes)
