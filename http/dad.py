import requests
import pyfiglet
import termcolor
from random import choice

header = pyfiglet.figlet_format("Dad Joke 3000")
header = termcolor.colored(header, color="blue")
print(header)
joke_status = True

while joke_status:
    term = input("Let me tell you a joke! Give me a topic: ")
    res_json = requests.get(
        "https://icanhazdadjoke.com/search",
        headers={"Accept": "application/json"},
        params={"term": term}
    ).json()

    results = res_json['results']
    total_jokes = res_json['total_jokes']
    if total_jokes > 1:
        print(
            f"I've got {total_jokes} jokes about {term}. Here's one:\n\n",
            choice(results)['joke']
        )
    elif total_jokes is 1:
        print(
            f"I've got one joke about a {term}. Here it is:\n\n",
            results[0]['joke']
        )
    else:
        print(
            f"\nSorry, I don't have any jokes about {term}! Please try again.")

    end = True
    while end:
        answer = input(
            "\nWould you like me to tell you another joke? [y/n]:\n")
        continue_ = answer.lower() + 'error_hack'
        if continue_[0] is 'n':
            joke_status = False
            end = False
            print("Bye!")
        elif continue_[0] is 'y':
            end = False
        else:
            print("Sorry, I didn't quite catch that.")
