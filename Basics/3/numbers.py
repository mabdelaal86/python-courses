#!/usr/bin/env python3

print("=======================")
print("Even Numbers in range 1:20")
for x in range(2, 21, 2):
    print(x)

print("=======================")
print("Odd Numbers in range 1:20")
for x in range(1, 21, 2):
    print(x)

print("=======================")
print("Numbers that dividable by 4 and 6 in range 1:100")
for x in range(1, 101, 1):
    if x % 4 == 0 and x % 6 == 0:
        print(x)
