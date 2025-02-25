"""Here we will learn about the strings."""
"""
String : String is a series of characters arranged in a sequential manner can be accessed through indexing. 
Strings are immutable which means once the string created can not be modified. 

1. Case Conversion Methods
--> capitalize() – Capitalizes the first character.
--> lower() – Converts all characters to lowercase.
--> upper() – Converts all characters to uppercase.
--> title() – Capitalizes the first character of every word.
--> swapcase() – Swaps case (uppercase becomes lowercase and vice versa).

2. Search and Replace Methods
--> find() – Returns the index of the first occurrence of a substring; returns -1 if not found.
--> rfind() – Returns the index of the last occurrence of a substring.
--> index() – Same as find(), but raises a ValueError if the substring is not found.
--> rindex() – Same as rfind(), but raises a ValueError if not found.
--> replace() – Replaces occurrences of a substring with another substring.
--> count() – Returns the number of occurrences of a substring.

3. String Splitting and Joining Methods
--> split() – Splits a string into a list based on a separator.
--> rsplit() – Splits a string from the right side.
--> splitlines() – Splits a string at line breaks (\n).
--> join() – Joins elements of a list into a string, using the string as a separator.
--> partition() – Splits a string into three parts at the first occurrence of a separator.
--> rpartition() – Splits a string into three parts at the last occurrence of a separator.

4. Whitespace and Padding Methods
--> strip() – Removes leading and trailing whitespace.
--> lstrip() – Removes leading whitespace.
--> rstrip() – Removes trailing whitespace.
--> center() – Centers the string, padding it with a specified character.
--> ljust() – Left-aligns the string, padding it with a specified character.
--> rjust() – Right-aligns the string, padding it with a specified character.
--> zfill() – Pads the string with zeros on the left.

5. Boolean Methods (Return True or False)
--> startswith() – Checks if the string starts with a specified prefix.
--> endswith() – Checks if the string ends with a specified suffix.
--> isalpha() – Returns True if all characters are alphabetic.
--> isdigit() – Returns True if all characters are digits.
--> isalnum() – Returns True if all characters are alphanumeric.
--> isspace() – Returns True if all characters are whitespace.
--> islower() – Returns True if all characters are lowercase.
--> isupper() – Returns True if all characters are uppercase.
--> istitle() – Returns True if the string is in title case.
--> isnumeric() – Returns True if all characters are numeric.
--> isdecimal() – Returns True if all characters are decimal numbers.

6. Encoding and Formatting Methods
--> encode() – Encodes the string into bytes using the specified encoding.
--> format() – Formats the string using placeholders.
--> format_map() – Formats the string using a dictionary.
--> maketrans() – Creates a translation table for use with translate().
--> translate() – Replaces characters based on a translation table.

7. Miscellaneous Methods
--> len() – Returns the length of the string (not technically a method, but a built-in function).
"""
sample_string = "ambivert"

# String indexing - we can access the characters by using indexing. Starting index will start from 0 and upper index len string - 1.
print(sample_string[0])

print(sample_string[4])

print(sample_string[len(sample_string) - 1])

# String methods
# Title method - Used to convert first character of the string in each and every word to upper case.
print(f"Title method : {sample_string.title()}")

# Upper method - Used to convert all characters in a string to the upper case.
print(f"Upper method : {sample_string.upper()}")

# Lower method - Used to convert all characters in a string to the lower case.
print(f"Lower method : {sample_string.lower()}")

# Find method - Used find the sub string in the given range.String index will be optional.
print(f"Find method : {sample_string.find('i', 0, 8)}")

# Capitalize method - Used to convert first letter of string to the upper case.
print(f"Capitalize method : {sample_string.capitalize()}")

# Center method - Used to move string to the center and fill with come character. Fill character is option by default " "
print(f"Center method : {sample_string.center(20,'-' )}")

# Count method - Used to count character occurrence in the given range. Range will be optional.
print(f"Count method : {sample_string.count('i', 0, 8)}")

# Endswith method - Used to find given string end with particular character. Range will be option.
print(f"Endswith method : {sample_string.endswith('t', 0, 8)}")

# Starswith method - Used to find given string start with particular character. Range will be option.
print(f"Startswith method : {sample_string.startswith('a', 0, 8)}")

# Isalnum method - Used to find string contain all alphanumeric characters. Like characters and numbers.
print(f"Isalnum method : {sample_string.isalnum()}")

# Isascii method - Used to find string contain all ascii characters. Like ascii range 0 - 127.
print(f"Isascii method : {sample_string.isascii()}")

# Index method - Used to find index of character in a given string. Range is optional.
print(f"Index method : {sample_string.index('t', 0, 8)}")

# Isalpha method - Used to find string will contain only alpha characters.
print(f"Isalpha method : {sample_string.isalpha()}")

# Isdecimal method - Used to find given string only numbers.
print(f"Isdecimal method : {sample_string.isdecimal()}")

# Isdigit method - Used to find given string only numbers if any superscripts are also there it will return True.
print(f"Isdigit method : {sample_string.isdigit()}")

# Is identifier method -  Used to find string contain characters and underscore and python keywords.
print(f"Is identifier method : {sample_string.isidentifier()}")

# Islower method - Used to find all characters in a string lower case letters.
print(f"Islower method : {sample_string.islower()}")

# Is printable method - Used to find all characters in a string can print.
print(f"Is printable method : {sample_string.isprintable()}")

# Isnumeric method - Used to find given string will contain numeric characters.
print(f"Isnumeric method : {sample_string.isnumeric()}")

# Isspace method - Used to find string contain any spaces.
print(f"Isspace method : {sample_string.isspace()}")

# Istitle method - Used to find given string is in title case.
print(f"Istitle method : {sample_string.istitle()}")

# Isupper method - Used to find all characters in a string are upper case.
print(f"Isupper method : {sample_string.isupper()}")

# Join method - Used to join string with the other iterable.
print(f"Join method : {sample_string.join('MU')}")

# Expand tab method - If string contain any tab method it will expand defined size.
sample_string = "Hello\tworld..!"
print(f"Expandtabs method : {sample_string.expandtabs(10)}")

# Format map method - Format map method is used connect dictionary objects to string
sample_dict = {"name": "Jhon", "age" : 27}
text = "My name is {name}.And i am {age} old."
formated_text = text.format_map(sample_dict)
print(f"Format_map method : {formated_text}")

# ljust method - Ljust method is used to left justify the text in the given range.
sample_string = "ambivert"
print(f"Ljust method : {sample_string.ljust(25, '-')}")

# lower method - Lower method is used to convert all upper case letters to the lower case.
print(f"Lower method : {sample_string.lower()}")

# l strip method - L strip method is used to remove any character from the left side of the string
print(f"L strip method : {sample_string.lstrip('a')}")

# r strip method - R strip method is used to remove any character from the right side of the string
print(f"R strip method : {sample_string.rstrip('t')}")

# make trans method  - Make trans method is used to replace character will the anthor characters.
# trans_table = str.maketrans("ae", "12")
# formated_text = sample_string.maketrans(trans_table)
# print(f"Make trans method : {formated_text}")

# Partition method - Partition method is used to break the given sentence into the tuple based on given by the argument.
print(f"Partition method : {sample_string.partition('v')}")

# Remove prefix method - Remove prefix method is used to remove any given argument at starting position of the string.
print(f"Remove prefix method : {sample_string.removeprefix('a')}")

# Remove suffix method - Remove prefix method is used to remove any given argument at starting position of the string.
print(f"Remove suffix method : {sample_string.removesuffix('t')}")

# Replace method - Replace method is used change old character to new character. Count is optional if we won't specify anything it will replace everything otherwise it will replace max no.of occurrences.
print(f"Replace method : {sample_string.replace('a', 'b', 1)}")

# Rfind method - Rfind method is used to find characters from right side in the given range.
print(f"Rfind method : {sample_string.rfind('t', 0, 8)}")

# Rindex method - Rindex method is used to find index of the given argument. If string not it will raise error.
print(f"Rindex method : {sample_string.rindex('a', 0, 8)}")

# Rjust method - It is used to align the text with the given size and fill characters.
print(f"Rjust method : {sample_string.rjust(10, ' ')}")

# Rpartition method - Rpartition method is used to partition the string from the right side.
print(f"Rpartition method : {sample_string.rpartition('v')}")

# Rsplit method - Rsplit method is used to split the string based on given arguments from the right side.
print(f"Rsplit method : {sample_string.rsplit('v',1)}")

# Rstrip method - Rstrip method is used to remove characters from the right side.
print(f"Rstrip method : {sample_string.rstrip('t')}")

# Split method - Split method is used to split the string based on given argument.
print(f"Split method : {sample_string.split('v')}")

# Splitlines method - Splitlines method is used to split string based on any '\n' inthe string.
print(f"Splitlines method : {sample_string.splitlines()}")

# Swapcase method - Swapcase method is used to change uppercase letters to lowercase and uppercase.
print(f"Swapcase method : {sample_string.swapcase()}")






