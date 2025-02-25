"""Here we will learn about different operations performed in python"""
# Python operations
"""
Python operations : Python operations will help us to perform certain actions. In python various different types of operations are there 

Arithmetic operations : Arithmetic operations are help to perform the mathematical operations. Such as addition, subtraction, multiplication, division, exponent..
Comparison operations : Comparison operators are to compare between the two values . Such as equal, less than, greater than, less then or equal, greater than or equal, not equal...
Assignment operations : Assignment operations are assign particular value to given variable or existing variable which already contain value. assign, add and assign, subtract and assign, multiply and assign, division and assign, floor division and assign, modulo and assign, exponent and assign..
Logical operations : Logical operations will help us to evaluate multiple expressions. Such as and, or, not..
Bitwise operations : Bitwise operations will perform on os level it will convert decimal to binary and perform actions. Such as and(&), or(|), xor(^), not(~), leftshift(<<), rightshift(>>)..
Membership operations : Membership operator help to perform element is present or not. Such as in, not in..
Identity operations : Identity operator used to compare the memory address of the element.
"""
first_variable = 25
second_variable = 5

# Arithmatic operations - Addition, Subtraction, Multiplication, Division - Normal division, Floor division, Modulo, exponent.
# Addition - Addition will perform to adding of two numbers
addition = first_variable + second_variable
print(f"Addition of two numbers : {addition}")

# Subtraction - Subtraction will perform to subtraction between two numbers
subtraction = first_variable -  second_variable
print(f"Subtraction of two numbers : {subtraction}")

# Multiplication - Multiplication will perform to multiply two numbers
multiplication = first_variable *  second_variable
print(f"Multiplication of two numbers : {multiplication}")

# Division - Division will perform to divide two numbers - Normal division
division = first_variable /  second_variable
print(f"Division of two numbers : {division}")

# Floor division - Floor division will perform to divide two numbers and will get integer as output - Floor division
floor_division = first_variable //  second_variable
print(f"Floor division of two numbers : {floor_division}")

# Modulo - Modulo will perform to get reminder from the given numbers
modulo = first_variable %  second_variable
print(f"Modulo of two numbers : {modulo}")

# Exponent - Exponent will perform to make the number to power of x.
exponent = first_variable **  second_variable
print(f"Exponent of two numbers : {exponent}")


# Comparison operations : Equal, Not equal, Less than, Greater than, Less than or equal, Greater than or equal.
# Equal : Equal is used to compare the values or equal or not.
print(f"Given values are equal : {first_variable == second_variable}")

# Not equal : Not equal is used to compare the values not equal or equal.
print(f"Given values are not equal : {first_variable != second_variable}")

# Less than : Less than is used to compare the first value is smaller than the second value.
print(f"First value smaller than second value : {first_variable < second_variable}")

# Greater than : Greater than is used to compare the first value is bigger than the second value.
print(f"First value bigger than second value : {first_variable > second_variable}")

# Less than or equal : Less than or equal is used to compare the first value is smaller or equal to the second value.
print(f"First value smaller or equal to second value : {first_variable <= second_variable}")


# Greater than or equal : Greater than or equal is used to compare the first value is smaller or equal to the second value.
print(f"First value bigger or equal to second value : {first_variable >= second_variable}")

# Assignment operations : Assign, Add and assign, Subtract and assign, Multiply and assign, Division and assign, Floor division and assign, Modulo and assign, Exponent and assign.
# Assign : To assign value to the variable
assign_variable = 5
print(f"Assign variable : {assign_variable}")

# Add and assign : To perform addition on already existing variable.
first_variable += assign_variable
print(f"Add and assign to variable : {first_variable}")

# Subtract and assign : To perform subtraction on already existing variable.
first_variable -= assign_variable
print(f"Subtract and assign to variable : {first_variable}")

# Multiply and assign : To perform multiplication on already existing variable.
first_variable *= assign_variable
print(f"Multiplication and assign to variable : {first_variable}")

# Divide and assign : To perform Division on already existing variable.
first_variable /= assign_variable
print(f"Division and assign to variable : {first_variable}")

# Floor division and assign : To perform floor division on already existing variable.
first_variable //= assign_variable
print(f"Floor division and assign to variable : {first_variable}")

# Modulo and assign : To perform Modulo on already existing variable.
first_variable %= assign_variable
print(f"Modulo and assign to variable : {first_variable}")

# exponent and assign : To perform exponent on already existing variable.
first_variable **= assign_variable
print(f"Exponent and assign to variable : {first_variable}")


# Logical operations : And, Or, Not
# And : If both expressions in a given statement are true then it will be return true.
print(f"Logical expression for and : {first_variable == 0 and second_variable > 0}")

# Or : If any one expression true in given statement it will return true.
print(f"Logical expression for or : {first_variable == 0 and second_variable == 0}")

# Not : Not statement will return opposite to actual statement.
print(f"Logical expression for not : {not first_variable == 0}")


# Bitwise operations : And, Or, XOR, Not, Leftshift, Rightshift - Bitwise operations are perform at the os level it will contain 0 and 1.
# And (&) : Both are true then it will true.
first_variable = 7  # 111
second_variable = 5 # 101
print(f"Bit wise and operation : {first_variable and second_variable}") # 0101

# Or (&) : Any one true then it will true.
first_variable = 7  # 111
second_variable = 5 # 101
print(f"Bit wise or operation : {first_variable or second_variable}") # 0111

# XOR (^) : If any one value true it will true else false. Like if both the true or false cases it will return false.
first_variable = 7  # 111
second_variable = 5 # 101
print(f"Bit wise XOR operation : {first_variable ^ second_variable}") # 010

# Not (~) : Not will perform on single variable in this zeros will become ones and ones become zeros.
first_variable = 7  # 111
print(f"Bit wise Not operation : {~ first_variable}") # ~ first_variable = -(first_variable + 1)

# Left shift (<<) : It will push the binary places to the left side. number will represent how many push are done
first_variable = 7  # 111
print(f"Bit wise left shift operation : {first_variable << 1}") # Shift value 1 it will be 1110 , Shift value two it will be 11100.

# Right shift (<<) : It will push the binary places to the right side. number will represent how many push are done
first_variable = 7  # 111
print(f"Bit wise left shift operation : {first_variable >> 1}") # Shift value 1 it will be 0011 , Shift value two it will be 0001.


sample_list = [2, 4, 6, 8, 10]
# Membership operator : in, not in
# In operator : It is evaluated the element present in object or not.
print(f"In operator for list : {7 in sample_list}")

# Not in operator : It is evaluated the element present not to be in object.
print(f"Not in operator for list : {7 not in sample_list}")


# Identity operator : Is, Is not
# Is operator : It is used compare the memory address of the objects.
print(f"Is operator for comparing objects : {second_variable is assign_variable}")

# Is not operator : It is used to compare memory address for the negative scenario.
print(f"Is not operator for comparing objects : {second_variable is not assign_variable}")








