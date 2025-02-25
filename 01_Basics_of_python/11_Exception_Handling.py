""" Here will learn about the Exception handling """
"""
Exception handling : Exceptions are any unexpected event happen while running in the program. When any exception happen 
program will going crash. To aviod that we can use exception handling techniques.
To handle the exceptions we will use try, except block to handling errors carefully.
"""

# Try - except block
try:
    num = int(input("Enter number to divide : "))
    result = 10 / num
    print(result)
except ZeroDivisionError as e:
    print(f"ZeroDivisionError : {e}")

# Handling multiple error types
try:
    num = int(input("Enter number to divide : "))
    result = 10 / num
    print(result)
except (ZeroDivisionError, ValueError) as e:
    print(f"Error : {e}")

# Handling exception with the else block. Else block will run if no errors are occurred.
try:
    num = int(input("Enter number to divide : "))
    result = 10 / num
except ZeroDivisionError as e:
    print(f"Error : {e}")
else:
    print(f"Result : {result}")

# Finally block. Finally block will execute with respect anything at end it will run.
try:
    num = int(input("Enter number to divide : "))
    result = 10 / num
except ZeroDivisionError as e:
    print(f"Error : {e}")
else:
    print(f"Result : {result}")
finally:
    print("Execution completed.")


# Raise an exception
num = int(input("Enter a positive number : "))
if num < 0:
    raise ValueError("The number must be positive..")

# Raise an custom exception
class NegativeNumberError(Exception):
    pass

num = int(input("Enter a positive number : "))
if num < 0:
    raise NegativeNumberError("Negative numbers are not allowed..")





