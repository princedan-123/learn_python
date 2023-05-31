#!/bin/python3
#checks a voters eligibility based on age
age = input('please enter your age\n')
age = int(age)
if age >= 18:
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')
