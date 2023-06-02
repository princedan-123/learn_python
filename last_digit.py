#!/bin/python3
from random import randint
# write a script that prints the last digit of a randomly generated number

n = randint(10, 1000)
print('the generated number is',n)
if n < 100:
    print('the last digit is', n%10)
elif n in range(100, 110):
    print('the last digit is', n % 100)
elif n in range(110, 1000):
     n = n % 100
     print('the last digit is', n % 10)
elif n == 1000:
    print('the last digit is', n % 1000)
