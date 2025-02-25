""" Here we will learn about the random module """
import random
"""
Random module will help us to generate objects randomly.
"""

# Randint method - It will generate random number in the given range. It will include both upper and lower bounds.
print(f"Random number : {random.randint(1, 10)}")

# Random method - It will generate the decimal value in between 0 and 1. It will include lower bound not upper bound.
print(f"Random decimal value in between 0 to 1 : {random.random()}")

# Choice method - It will pick up random item from the list.
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Random value from the list : {random.choice(random_list)}")

# Uniform method - Uniform method is used generate random number between the given the range including lower and upper bound.
print(f"Random uniform value in between 0 to 1 : {random.uniform(0, 1)}")

# Randrange method - It will generate the random number between given range with an defined step.
print(f"Randrange value in between 0 to 50 with step 5 : {random.randrange(0, 50, 5)}")

# Choices method - It will give us random number with the desired quantity. It will give same number multiple times.
print(f"Random values with choices method in a list : {random.choices(random_list, k = 3)}")

# Sample method - It will give us random numbers with desired quantity. It will always give us the unique numbers.
print(f"Random values with sample method in a list : {random.sample(random_list, k = 3)}")

# Shuffle method - It will shuffle all elements in the list
random.shuffle(random_list)
print(f"Shuffled list : {random_list}")

# Seed method - Seed method is used get get same number how many times you will generate. It will help us for the debugging purpose.
random.seed(7)
print(f"Choice method using seed : {random.random()}")



