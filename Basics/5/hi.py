#!/usr/bin/env python3

def welcome():
    print("Welcome")

def hi(name):
    print("Hi " + name + "!")

welcome()
username = input("Who are there? ")
hi(name=username)
hi(username)
