"""
What is programing and why programing:
Programing is set of instructions give to system to perform certain operations.
Computer cont able to do anything by their own it need instructions to perform certain task.

Why python:
Python is very versatile programing language with easy syntax and dynamic typing. It can be used in the various fields such
as web applications, mobile applications, gaming applications, machine learning, artificial intelligence, data science many more..

Unique properties of python:
High level language - Human readable code
Easy syntax - Mostly like an english language
Use cases - Python is used in various different fields
Interpreted language - Python is Interpreted language debugging is easy

Installation of Python:
Python installation is very easy either can download from the ms store or download from official website and installation is very easy.

REPL function:
R - Read
E - Evaluate
P - Print
L - Loop

What is pip:
Pip is a package manager to install external library.
"""

# Print function
""" 
Print function is used print result to console. Print function has different arguments
Values - It will print any value or expression
Sep - Sep will help us to distinguish between two variables. Default - " "
End - End is used to append items to previous print function. Default - "\n"
File - Print something to file directly.
Flush - Forcefully print something to stream. Default - False
"""
a = 5
b = 7

print("Normal print function : {a}")
print(f"Print function with sep : {a}", f"{b}", sep = " - ")
print(f"Print function with end : {a}", end = " ")
print(b)

# Input function
"""
Input function is used to take input from the user.
While using input function if you pass int, float values it will be treated as string later we need to change as per requirement.
"""
print("You entered name : ",input("Hi..Welcome to programing world..! \nEnter your name: "))
