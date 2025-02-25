""" Here we will learn about the sys module """
import sys
"""
sys module : sys module will give access to the system specific arguments and function. Sys module is used manipulate
python runtime environment and interact with the interpreter. 
"""

# Print current file name
print(sys.argv)

# Exit from the program
print("Before exit")
#sys.exit(0)
print("This will not print")

# Get python version
print(sys.version)

# Get python version info
print(sys.version_info)

# List of paths
print(sys.path)

# Check platform
print(sys.platform)

# Recursion limit
print(sys.getrecursionlimit())

# Size of an object
num = 25
print(sys.getsizeof(num))

# Python interpreter path
print(sys.executable)
