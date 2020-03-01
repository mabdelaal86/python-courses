#!/usr/bin/env python3

# inputs
num = int(input("Enter a number: "))

# processing
if num % 2 == 0:
    result = "Even"
else:
    result = "Odd"

# outputs
print("You entered", result, "number")
