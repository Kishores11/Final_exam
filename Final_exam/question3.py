import math

def fact():
    num = int(input("Enter an non-negative integer:"))
    if num > 0:
        fact = math.factorial(num)
        print(f'The factorial of {num} is {fact}.')
    else:
        return "Please enter value above zero"

message = fact()
print(message)