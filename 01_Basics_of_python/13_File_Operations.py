""" In this module we will learn about the file operations."""
"""
File operations : File operations will consist of the multiple operations such as like read, write, append..etc
"""
# Write to file : If we want to write something to file we can use 'w' tag and write something to file. If file not exist it will create new file.
# If we are using file with the write mode if any content already in file it will replace with the new content.
file = open('sample.txt', 'w')
file.write('Hello, everyone...! \nHello, world...! \nHello, python...!')
file.close()

# Read from file : We can read from the files
file = open('sample.txt', 'r')
content = file.read()
print(content)
file.close()

# Append content to files
file = open('sample.txt', 'a')
file.write('\nHello, Python coders...!')
file.close()

# Read file line by line
file = open('sample.txt', 'r')
for line in file:
    print(line.strip())
file.close()

# Seek - Seek will pointer to the required position
# Tell - Tell will give us current pointer position
file = open('sample.txt', 'r')
print(file.tell())
file.seek(10)
print(file.tell())
file.close()












