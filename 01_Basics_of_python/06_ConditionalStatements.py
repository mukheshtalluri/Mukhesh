""" Here will learn about the conditional statements """
"""
Conditional statements : Conditional statements evaluate the expression and take decision based on the expression.
There three conditional statements are there will discuss one by one.

If statement : If statement is used to evaluate the expression.
Elif statement : Elif statement is used to execute when the if statement will fail it will come to elif statement but it is optional.
Else statement : Else statement will execute if every thing will fail at end else statement will execute.

By using these we can make normal conditional statements and nested conditional statements.
"""

# Conditional statement with the if-else condition.
number = 5
if number % 2 == 0:
    print(f"{number} is Even number.")
else:
    print(f"{number} is Odd number.")


# Conditional statement with the if-elif-else condition. We can use as many as elif as per our of requirement.
gender = 'male'
if gender == 'male':
    print("Your are a male.")
elif gender == 'female':
    print("Your are a female.")
else:
    print("Your gender is not specified.")


# Nested conditional statements - if condition applied inside the anthor conditional statement.
number = 55
if number % 2 == 0:
    if number < 50:
        print("Given number is Even number and less than 50.")
    elif number < 100:
        print("Given number is Even number and less than 100.")
    else:
        print("Given number is Even number and high number.")
else:
    if number < 50:
        print("Given number is Odd number and less than 50.")
    elif number < 100:
        print("Given number is Odd number and less than 100.")
    else:
        print("Given number is Odd number and high number.")




