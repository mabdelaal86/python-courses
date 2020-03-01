#!/usr/bin/env python3

def avg(l):
    return sum(l) / len(l)

l = []
for x in range(7):
    d = int(input("Enter a number: "))
    l += [d]

print("Average=", avg(l))
