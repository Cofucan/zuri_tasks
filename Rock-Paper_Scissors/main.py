import random

options_l = ['r', 'p', 's']
options_w = ['rock', 'paper', 'scissors']
outcomes = ['R - Rock', 'P - Paper', 'S - Scissors']
record = {'r': 'rock', 'p': 'paper', 's': 'scissors'}


print('Welcome to our game of Rock-Paper-Scissors')

player_win = 0
cpu_win = 0

while True:
    while True:
        print('Pls enter one of the 3 options below')
        for item in outcomes:
            print(item)
        player_choice = input('Enter the letter or the word: ').lower()

        is_letter = player_choice in options_l
        is_word = player_choice in options_w

        if is_letter:
            player_choice = record[player_choice]
            break
        elif is_word:
            break

        print('Sorry! Worng input')
        continue

    cpu_choice = random.choice(options_w)

    print(f'Player {player_choice} : CPU {cpu_choice}')

    if player_choice == ('rock') and cpu_choice == ('paper'):
        print('Sorry! You lost \n')
        cpu_win += 1
    elif player_choice == ('paper') and cpu_choice == ('rock'):
        print('Congrats! You won \n')
        player_win += 1
    elif player_choice == ('rock') and cpu_choice == ('scissors'):
        print('Congrats! You won \n')
        player_win += 1
    elif player_choice == ('scissors') and cpu_choice == ('rock'):
        print('Sorry! You lost \n')
        cpu_win += 1
    elif player_choice == ('paper') and cpu_choice == ('scissors'):
        print('Sorry! You lost \n')
        cpu_win += 1
    elif player_choice == ('scissors') and cpu_choice == ('paper'):
        print('Congrats! You won \n')
        player_win += 1
    else:
        print('Ok that was a tie so we have go again.')
        continue

    try_again = input('Do you want to try again? \n y / n \n')

    if try_again == 'n':
        print('\nHere are the scores')
        print(f'You : {player_win}')
        print(f'CPU : {cpu_win}')

        if player_win > cpu_win:
            print('You win the game!')
        elif player_win < cpu_win:
            print('CPU wins the game')
        else:
            print('The game was a tie')

        break
