#!/bin/python3
#!/bin/python3
#guess a number game
from sys import exit
from random import randint
num = randint(1, 100)
attempt = 1
guess = int(input('i am thinking of a number, please guess the number or type 0 to exit\n'))
while guess != num and attempt != 6:
    if guess > num:
        guess = int(input('the number is higher than what i thought of, guess again\n'))
    elif guess < num:
        guess = int(input('the number is less than what i thought of, guess again\n'))
    if guess == 0:
        exit()
    attempt += 1
if guess == num and attempt == 1:
    print('!wow you are a mind reader, you got the answer')
elif guess == num and attempt != 0:
    print('you got the answer after', attempt,  ' attempts')
elif attempt >= 6:
    print('exceeded five attempts, the answer is', num)

