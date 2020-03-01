#!/usr/bin/env python3

# inputs
num = int(input("Enter a number: "))

# processing
if num > 0:
    result = "Positive"
elif num < 0:
    result = "Negative"
else:
    result = "Zero"

# outputs
print("You entered", result, "number")
