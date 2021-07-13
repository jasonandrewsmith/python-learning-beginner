import random

while(True):
    cpu_choice = random.choice(['scissors', 'rock', 'paper'])
    user_choice = input('rock, paper, or scissors?\n')

    if cpu_choice == user_choice:
        print('TIE')
    elif user_choice == 'rock' and cpu_choice == 'scissors':
        print('WIN')
    elif user_choice == 'paper' and cpu_choice == 'rock':
        print('WIN')
    elif user_choice == 'scissors' and cpu_choice == 'paper':
        print('WIN')
    else:
        print('YOU LOST')