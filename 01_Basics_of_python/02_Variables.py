""" In this session we will learn about the variables."""
# Variables
"""
Variable : Variable are the containers which will hold the data. Data can be in any from like int, float, str..

Variable naming convention:
Normally we can define variables with any name but it is better to follow the standards. Never use key words as variables.
Variables wont contain any spaces and special characters and never start with numbers and we can underscore in middle or end.
PascalCase : Each word first letter will be capital letter and  remaining all are small letters. Ex - EnterName
camelCase : First word first letter will be small and remaining words first letter will be capital letter and remaining letters will be small letters. Ex - enterName
snake_case : every letter small letter and word to word variation we can do with the underscore. Ex - enter_name

This is standards not only for the variables we can use for the class names and method names and function names.
"""
integer_value = 5
print(f"Integer value : {integer_value}")

float_value = 12.33
print(f"Floating value : {float_value}")

string_value = "Python"
print(f"String value : {string_value}")

# Different way to print using placeholders, format, f-strings.
sample_variable = 5
sample_float = 12.4
print(sample_variable)

# If we want to print same variable along with some text it will throw error.
# Type Error : TypeError will occur when we are trying to add two different data types.
try:
    print("Sample variable : " + sample_variable)
except TypeError as e:
    print(f"TypeError : {e}")

# There are different methods to concatenate two different datatypes.
# Using placeholders - %s for string, %r for repr, %d for digit, %f for floating points
"""
Place holders:
%s - It will represent the string  and it is used to pass any string variables.
%r - It will represent the raw string. Like if any tab or special characters will be there in the string it will print alog with the special meaning.
%d - It will represent the whole numbers.
%f - It will represent the decimal numbers. we can make precision also from by using this place holder. Ex- % 5.3f Total it will allow 5 numbers along with the 3 decimal values.
"""
print("Sample variable print with an place holder :  %d." % sample_variable)
print("Multiple variables print with place holders : %d and %f" %(sample_variable, sample_float))

# Using format method - Using format method we can print multiple variables with by providing positions index and we can do alignments as well.
print("Sample variable print with format method : {}".format(sample_variable))
print("|{0:10} | {1:10} | {2:10}|".format("First name", "Middle name", "Last name"))
print("|{0:<15} | {1:^15} | {2:>15}|".format("First name", "Middle name", "Last name"))
print("|{0:-<15} | {1:#^15} | {2:*>15}|".format("First name", "Middle name", "Last name"))

# Using f-string
print(f"Sample variable print with the f-strings : {sample_variable}")







