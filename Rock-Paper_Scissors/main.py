import random

options_l = ['r', 'p', 's']
options_w = ['rock', 'paper', 'scissors']
outcomes = ['R - Rock', 'P - Paper', 'S - Scissors']
record = {'r': 'rock', 'p': 'paper', 's': 'scissors'}


print('Welcome to our game of Rock-Paper-Scissors')

user_win = 0
cpu_win = 0

while True:
    while True:
        print('Pls enter one of the 3 options below')
        for item in outcomes:
            print(item)
        user_choice = input('Enter the letter or the word: ').lower()

        is_letter = user_choice in options_l
        is_word = user_choice in options_w

        if is_letter:
            user_choice = record[user_choice]
            break
        elif is_word:
            break

        print('Sorry! Worng input')
        continue

    cpu_choice = random.choice(options_w)

    print(f'Player {user_choice} : CPU {cpu_choice}')

    if user_choice == ('rock') and cpu_choice == ('paper'):
        print('Sorry! You lost')
        cpu_win += 1
    elif user_choice == ('paper') and cpu_choice == ('rock'):
        print('Congrats! You won')
        user_win += 1
    elif user_choice == ('rock') and cpu_choice == ('scissors'):
        print('Congrats! You won')
        user_win += 1
    elif user_choice == ('scissors') and cpu_choice == ('rock'):
        print('Sorry! You lost')
        cpu_win += 1
    elif user_choice == ('paper') and cpu_choice == ('scissors'):
        print('Sorry! You lost')
        cpu_win += 1
    elif user_choice == ('scissors') and cpu_choice == ('paper'):
        print('Congrats! You won')
        user_win += 1
    else:
        print('Ok that was a tie so we have go again.')
        continue

    try_again = input('Do you want to try again? \n y / n \n')

    if try_again == 'n':
        print('Here are the scores')
        print(f'You : {user_win}')
        print(f'CPU : {cpu_win}')

        if user_win > cpu_win:
            print('You win the game!')
        elif user_win < cpu_win:
            print('CPU wins the game')
        else:
            print('The game was a tie')

        break
