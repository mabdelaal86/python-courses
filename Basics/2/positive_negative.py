#!/usr/bin/env python3

num = int(input("Enter a number: "))

if num > 0:
    result = "Positive"
elif num < 0:
    result = "Negative"
else:
    result = "Zero"

print("You entered", result, "number")