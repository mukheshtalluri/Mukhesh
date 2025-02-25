"""In this session we will learn about the lambada function"""
"""
Lambda function : Lambda is an small anonymous function which will take any number of arguments and return single output.
Lambda can be used with the some other functions like map, filter reduce..etc
"""
addition = lambda x, y : x + y
print(f"The addition of above numbers : {addition(5, 6)}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = lambda x : x % 2 != 0
print(list(filter(odd_numbers, numbers)))
