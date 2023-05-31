#!/bin/python3
#checks the greater number between to input integers
num1 = input('enter any number\n')
num1 = int(num1)
num2 = input('enter another number\n')
num2 = int(num2)
if num1 > num2:
    print('the first number is greater than the second number\n')
elif num2 > num1:
    print('the second number is greater than the first number\n')
