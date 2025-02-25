""" Here we will learn about the recursion """
"""
Recursion : Recursion is type of function which call it self until the base condition is executed. 
Recursion implemented through stack memory and based condition is not satisfied it will lead to RecursionError.
"""

def first_method():
    second_method()
    print("First method executed.")

def second_method():
    third_method()
    print("Second method executed.")

def third_method():
    fourth_method()
    print("Third method executed.")

def fourth_method():
    print("Fourth method executed.")

first_method()

# Practical use of recursion - Factorial of number
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

print(f"The factorial of 5 : {factorial(5)}")

