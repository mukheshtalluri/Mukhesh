"""Here we will learn about the data types which were available in python."""
# Data types
"""
Data types : Data type will help us to kind of operations will perform on that variable. We have few data types

Numeric data : The data which is associated with the numeric data. Such as Integer, Float, Complex.
Text data : The data which is associated with the text. Such as Strings.
Boolean data : The data which will associated with the either true or false.
Sequence data : The data associated with the multiple values in sequential order. Such as List, Tuple.
Mapped data : The data which will refer one value to anthor value, Link between values. Such as Dictionary.
"""

# Type function
"""
Type function : Type function will help to find which kind of data hold by variable.
"""

# Numeric data
sample_integer = 5
sample_float = 10.53
print(f"Sample integer : {sample_integer}")
print(f"Data type of sample integer : {type(sample_integer)}")
print(f"Sample float : {sample_float}")
print(f"Data type of sample float : {type(sample_float)}")

# Text data - Text data will always embed between either single or double quotes.
sample_string = "Bangalore"
print(f"Sample string : {sample_string}")
print(f"Data type of sample string : {type(sample_string)}")

# Boolean data
sample_true = True
sample_false = False
print(f"Sample boolean : {sample_true}")
print(f"Data type of sample boolean : {type(sample_false)}")

# Sequence data
sample_list = [1, "List", 25.6]
sample_tuple = (2, "Tuple", 20,5)
print(f"Sample list : {sample_list}")
print(f"Data type of sample list : {type(sample_list)}")
print(f"Sample tuple : {sample_tuple}")
print(f"Data type of sample tuple : {type(sample_tuple)}")

# Mapped data
sample_dictionary = {"name" : "Tom", "Age" : 25}
print(f"Sample dictionary : {sample_dictionary}")
print(f"Data type of sample dictionary : {type(sample_dictionary)}")

# Type casting

"""
Type casting - Type casting is way to convert one data type to the other data type.
Why Type casting : In the below sample we provided integer as the input but will data type. But it is string. In this scenarios we need to change them.
There are two ways of typecasting 
Implicit type casting : When we perform certain operations automatically data type of variable will change.
Explicit type casting : When we are converting data type it will be explicit type casting. 
"""

sample_input = input("Enter your age : ")
print(f"Sample input : {sample_input}. Type of sample input : {type(sample_input)}")

# Implicit type casting - we are performing operations on integers after certain operations it will convert to float.
num1 = 25
num2 = 5
result = 25 / 5
print(f"Implicit type casting integer is converted to float : {result} and Type of result {type(result)}.")

# Explicit type casting - we are change explicitly
sample_input = int(sample_input)
print(f"Explicit type casting string is converted to integer : {sample_input} and Type of result {type(sample_input)}.")


