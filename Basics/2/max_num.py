#!/usr/bin/env python3

# inputs
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))

# processing
if n1 >= n2:
    if n1 >= n3:
        x = n1
    else:
        x = n3
else:
    if n2 >= n3:
        x = n2
    else:
        x = n3

# outputs
print("Max=", x)
