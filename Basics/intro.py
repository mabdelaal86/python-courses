#!/usr/bin/env python3

from datetime import date
from random import randint

print('Hello')

name = input('Who is there? ')

input(f'Hi {name}, How are you? ')

age = int(input('How old are you? '))

birth_year = date.today().year - age

print('So, you were born in', birth_year)

answer = input('Do you want to play a game? ').lower()

while answer not in ('yes', 'ok'):
    if answer in ('no', 'never'):
        answer = input('Why not, just one game? ')
    else:
        answer = input('What did you say? ')

print('Yessss, I love games')

my_num = randint(30, 50)
your_num = int(input('Can you guess the number that I\'m thinking of? '))

while your_num != my_num:
    if your_num < my_num:
        print("I'm thinking in a greater number than that!")
    else:
        print("I'm thinking in a smaller number than that!")
    your_num = int(input("Enter another one: "))

print('\nYou got it. Great work')
print('It is a great pleasure to talk with you')
print('\nI have to leave now, Goodbye')
