import random

# Rock paper scissors terminal
print('Welcome to Rock Paper Scissors \n')
prompt = "1: 'Rock' \n2: 'Paper' \n3: 'Scissors' \nEnter your choice: "
p1_choice = input(prompt)
p2_choice = random.randint(1, 3)
result = ''

if(p1_choice == p2_choice):
    result = 'tie'

if(p1_choice == 1):
    if(p2_choice == 2):
        result = 'player 2 wins'

    if(p2_choice == 3):
        result = 'player 1 wins!'


print(result)
