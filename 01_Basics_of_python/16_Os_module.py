""" Here we will learn about the os module """
import os
"""
Os module : Os module is used to interact with the operating system.
"""
# Methods in os module

# Working with directory's
# Print the current working directory
print(f"Current working directory : {os.getcwd()}")

# Change the working directory
os.chdir(f"D:\\")
print(f"Current working directory : {os.getcwd()}")

# Print list of directory in current working directory
print(f"List of directory in current working directory : {os.listdir()}")

# Create a directory with os module
os.mkdir('Mukhesh')
print(f"List of directory in current working directory : {os.listdir()}")

# Create nested directory
os.makedirs(r'Test/Test_1')
print(f"List of directory in current working directory : {os.listdir()}")

# Remove directory
os.rmdir('Mukhesh')
print(f"List of directory in current working directory : {os.listdir()}")

# Remove nested directory
os.removedirs(r'Test/Test_1')
print(f"List of directory in current working directory : {os.listdir()}")

# Working with teh files
# Check the file exists in path
print(f"Check for the path existence : {os.path.exists('Python/01_Basics_of_python')}")

# Check it is file or directory
print(f"Check for it is file or directory : {os.path.isfile('run.bat')}")
print(f"Check for it is file or directory : {os.path.isdir('Python')}")

# Rename the file
#os.rename('run.bat', 'schedule.bat')

# Remove the file
#os.remove('schedule.bat')

print(os.name)



