#!/usr/bin/env python3

l = []
for x in range(7):
    d = int(input("Enter a number: "))
    l += [d]

avg = sum(l) / len(l)
print("Average=", avg)
