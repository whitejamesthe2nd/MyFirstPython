from random import *

guesses = 0
play_name = input('Please give me your name \n')
random_int = (random()*100)//1
v = False
while guesses<6:

    try:
        p_guess = int(input('Please guess a number one through 10 \n'))
        if p_guess < random_int:
            print('Higher')
        elif p_guess > random_int:
            print('Lower')
        elif p_guess == random_int:
            print('Just right')
            v= True
            break
        guesses += 1
    except:
        print('Please put in a number')
        continue
if v:
    print(f'Good Job {play_name}')
else:
    print('you suck jackass')
