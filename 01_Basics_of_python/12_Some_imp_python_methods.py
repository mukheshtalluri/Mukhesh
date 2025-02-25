""" Here we will discuss some special methods """
"""
Special methods : In python there some special methods are there which can help us in different ways.
Enumerate : Enumerate function is used to used to develop the counter to values of the iterables. and we can provide start number as well.
Map : Map is a function which can help to gave connection between the function and iterable.
Filter : Filter is used to filter values based on the condition.
Zip : Zip function is used to pack the one or more iterables.
Reduce : Reduce function is used to make iterable to single variables.
"""
# Enumerate function
sample_list = ['apple', 'box', 'cat', 'dog']
def sample_enumerate(list_items):
    for key, value in enumerate(list_items, start=100):
        print(f" {key} : {value} ")

sample_enumerate(sample_list)

# Map function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_numbers(num):
    if num % 2 == 0:
        return 'Even number'
    else:
        return 'Odd number'

print(list(map(even_numbers, numbers)))

# Filter function
def odd_numbers(num):
    if num % 2 != 0:
        return num

print(list(filter(odd_numbers, numbers)))

# Zip function
chars = ['a', 'b', 'c', 'd', 'e']
nums = [1, 2, 3, 4, 5]
print(list(zip(chars, nums)))

# Reduce function
from functools import reduce

def add(x, y):
    return x + y

sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)






