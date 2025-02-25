""" Here we will learn about the functions """

"""
Functions : Function is a block of code which is used to execute set of commands to reduce code redundancy and code maintenance.
There are two types of functions are there:
Built in function : Predefined will comes along with the python installation
User defined functions : User defined functions create by user as per the requirement.
"""

# Built in function - len, print, input
string = "orthodox"
print(f"Length of string : {len(string)}")

# User defined function
"""
User defined functions : User defined functions are functions which we create based on requirement.
Argument : Something we need to provide as input to function then it will be know as the argument.
There are different types of function are there
1. Default argument
2. Keyword arguments
3. Required arguments
4. Variable length arguments - arbitrary arguments, keyword arbitrary arguments
"""

# Default arguments : Default argument parameters we can defined while creating function itself.If we want to override them we can change them while run time.
# We need to remember while using default arguments try place default arguments at the end. and we need to maintain same order,
def person_info(name, language = 'Hindi', age = 25):
    print(f"My name is {name} and i am {age} old and i know {language}.")

person_info("Bob") # With the default parameters
person_info("Jock", "French", 37) # With override arguments.

# Keyword arguments : Keyword arguments are come with the key value pairs we can use in any order. And keyword are defined while run time.
def programing_info(lang, use_case):
    print(f"{lang} is mostly used in the {use_case}.")

programing_info(lang = 'Java', use_case = 'Web development')
programing_info(use_case = 'Machine learning', lang = 'Python') # In what ever position you defined the argument it will work without issue.

# Required arguments : Required are arguments are nothing but how many arguments we are define while defining function same no.of arguments we need to provide the run time.
def company_info(name, company, phone):
    print(f"My name is {name} and i am working in {company} and my phone number {phone}.")

company_info("Jack", "Google", "1234567890")

#Variable length arguments : We can provide any no.of arguments as required.
# Arbitrary arguments : we can provide as values as many as we want.
def addition(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(f"The sum of above numbers : {sum}.")

addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# Keyword arbitrary arguments : we need to provide as the keys and values.
def multiplication(**numbers):
    result = 1
    for key, value in numbers.items():
        result *= value
    print(f"The result of the all numbers : {result}.")

multiplication(a = 1, b = 2, c = 3, d = 4, e = 5)


"""
return : Return statement is used to function result stored as the variable and we use that where ever it is required.
"""

def subtraction(a, b):
    return f"The result : {a - b}"

print(subtraction(9, 2))


"""
Doc strings : Doc strings are which will give information about the function. We can provide function information next to the function definition.
We can read doc string information with mouse hoer to the function.
"""
def division(a, b):
    """Division we divide first number with the second number."""
    return f"The result : {a / b}"

print(division(35, 5))
