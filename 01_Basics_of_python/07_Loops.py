""" Here will learn about loops """
"""
Loop : Loop is which happening continuously. In Python we have two loops while loop and for loop.

While loop : While loop happen continuously until condition fail. If condition fail it dont enter into that loop as well.
For loop : For loop will run till elements in the iterable or range exits.

"""

# While loop - Sometimes while loop can create infinite loop if condition provide not properly.
i = 0
while i <= 10:
    print(i)
    i += 1

# For loop - We don't have infinite loop issue in the for loop, and it will run till range exists and iterable persists.
for i in range(10):
    print(i)

name = "ambivert"
for char in name:
    print(char)


# Range function
"""
Range function : Range function will help us generate the numbers in the given range and we can use them as indexes.
mainly range function will consist of the lower bound, upper bound, step definition.
lower bound : From which index loop need to be start we can define over there.
upper bound : Upto which index loop need to be run we can define in upper bound.
step definition : It will jump the index based on step definition.
"""
# Generate even numbers till 10 with the range function.
for i in range(2, 11, 2):
    print(i)


# Break and Continue
"""
Break : Break statement is used to break the loop when the condition is satisfied. Break statement will break entire loop. 
Continue : Continue statement is used to skip the current iteration.
"""
# Break
i = 0
while i < 10:
    if i == 7:
        break
    print(i)
    i += 1

# Continue
for i in range(11):
    if i == 3:
        continue
    print(i)






