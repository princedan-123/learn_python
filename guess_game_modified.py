#!/bin/python3
#guess a number game
num = 50
attempt = 1
guess = int(input('i am thinking of a number, please guess the number\n'))
while guess != num:
    if guess in range(45, 49) or guess in range(52, 56):
        guess = int(input('hmm, i think you are close keep guessing\n'))
    elif guess == 49 or guess == 51:
        guess = int(input('your are very close, keep guessing\n'))
    else:
        guess = int(input('guess again\n'))
    attempt += 1
if guess == num and attempt == 1:
    print('!wow you are a mind reader, you got the answer')
elif guess == num and attempt != 0:
    print('you got the answer after', attempt,  ' attempts')
