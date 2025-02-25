""" Here we will learn about the list, tuple, set, dictionary and their methods """
"""
With one variable we can store the only one value to over come this will use these data types.
1. List : List is an ordered data structure and mutable in nature and allow duplicates.
2. Tuple : Tuple is an ordered data structure and immutable in nature and will allow duplicates.
3. Set : Set is an unordered data structure and mutable and wont allow duplicates.
4. Dictionary : Dictionary is an mapped data structure and mutable and keys are unique.
"""

# List - Accessing all elements in a list using for loop.
my_list = ["apple", "boat", "cat", "dog", "elephant", "fox", "goat", "horse", "ice"]
for item in my_list:
    print(item)

# List methods
# Index method - Index method will give index position of the item.
print(f" Index method : {my_list.index("cat")}")

# Count method - Count method will give occurrence of item.
print(f" Count method : {my_list.count("apple")}")

# Pop method - Pop method will remove last item from the list.
print(f" Pop method : {my_list.pop()}")

# Append method - Append method will add item at the end of the list.
my_list.append("italy")
print(f" Append method : {my_list}")

# Remove method - Remove method is used to remove an item from the list with the defined value.
my_list.remove("cat")
print(f" Remove method : {my_list}")

# Insert method - Insert method is used to add an item to the list with required index and value.
my_list.insert(2, "camel")
print(f" Insert method : {my_list}")

# Extend method - Extend method is used to add an iterable to the list.
extend_list = ["jeep", "king", "large", "move"]
my_list.extend(extend_list)
print(f" Extend method : {my_list}")

# Reverse method - Reverse method is used to reverse the list.
my_list.reverse()
print(f" Reverse method : {my_list}")

# Sort method - Sort method is used to Sort the elements in a list to the ascending order.
my_list.sort()
print(f" Sort method : {my_list}")

# Clear method - Clear method is used to remove the elements from list.
my_list.clear()
print(f" Clear method : {my_list}")

# Copy method - Copy method is used to copy the elements from one list to other list.
"""
Copy method - There will be two way of copying one is shallow copying and other one deep copying
Shallow copy - Shallow copy will done with the help of copy method. and if you can any element in the parent list it wont change in the child list.
deep copy - Deep copy will done through assign list as a variable and in deep copy if you change anything if will change in the child method as well.
"""
sample_list = [1, 2, 3, 4, 5]

shallow_list = sample_list.copy()
print(f" Shallow copy list : {shallow_list}")

deep_copy = sample_list
print(f" Deep copy list : {deep_copy}")

# Id of all List - Id method will give us the memory location of object.
print(f" Sample list id : {id(sample_list)}")
print(f" Shallow copy list id : {id(shallow_list)}")
print(f" Deep copy list id : {id(deep_copy)}")

# Now i will perform some action parent list will see how both the list will behave
sample_list.append(7)
print(f" Shallow copy list : {shallow_list}")
print(f" Deep copy list : {deep_copy}")


# Tuple - Accessing elements in a tuple to using indexing. Tuple is immutable will have very few methods on tuple.
my_tuple = ("Abhi", "Babu", "chinna", "dhoni", "eega")
for i in range(len(my_tuple)):
    print(f"{my_tuple[i]}")

# Count method - Count method will count the occurrences of the elements.
print(f" Count method : {my_tuple.count('Abhi')}")

# Index method - Index method will give us index position of the element.
print(f" Index method : {my_tuple.index('Abhi')}")


# Set - Set is a unordered so we cont able to access through indexing. Set won't allow duplicates.
my_set = {"apple", "ant", "axe", "apricot", "ant"}
# My set will print only print one ant even though it was there in multiple times.
print(f"My set : {my_set}")

# Accessing elements from the set.
for item in my_set:
    print(item)

# Add method - Add method will add elements into the set.
my_set.add("arabic")
print(f"My set : {my_set}")

# Remove method - Remove method is used to remove item from the set.
my_set.remove('ant')
print(f"My set : {my_set}")

# Pop method - Pop method is used to remove an item from the list randomly.
my_set.pop()
print(f"My set : {my_set}")

# Update method - Update method is used to update the set the iterable.
update_list = ["box", "ball", "balloon", "bang"]
my_set.update(update_list)
print(f"My set : {my_set}")

# Discard method - In discard method if element not present in the set it won't through any error.
my_set.discard("beast")
print(f"My set : {my_set}")

# Clear method - Clear method will remove the all the elements from the list.
my_set.clear()
print(f"My set : {my_set}")

set_1 = {"ooty", "chennai", "bangalore", "mangalore", "hydrabad"}
set_2 = {"jaipur", "bangalore", "kolkata", "pune", "ooty"}

# Difference method - Difference method will help to find set1 elements which are not in set2.
print(f" Difference method : {set_1.difference(set_2)}")

# Intersection method - Intersection method will show common elements in the both the sets.
print(f" Intersection method : {set_1.intersection(set_2)}")

# Isdisjoint method - Isdisjoint method will return true when sets don't have any common elements else least one common element were present it will return false.
print(f" Isdisjoint method : {set_1.isdisjoint(set_2)}")

# Issubset method - All elements in set1 were present in set2 then it will be return true else false.
print(f" Issubset method : {set_1.issubset(set_2)}")

# Issuperset method - All elements in set2 were present in set1 then it will be return true else false.
print(f" Issuperset method : {set_1.issuperset(set_2)}")

# Union method - Union method will print all elements from the both the sets.
print(f" Union method : {set_1.union(set_2)}")

# Symmetric difference method - This method will print the unique elements from the both the sets.
print(f" Symmetric difference method : {set_1.symmetric_difference(set_2)}")

# Difference update method - This method update set1 to no set2 elements in the set1.
set_1.difference_update(set_2)
print(f" Difference update method : {set_1}")

# Intersection update method - This method will update set1 to common elements in the both the sets.
set_1.intersection_update(set_2)
print(f" Intersection update method : {set_1}")

# Symmetric difference update method - This method will update set1 to all elements in the both the set without common elements.
set_1.symmetric_difference_update(set_2)
print(f" Symmetric difference update method : {set_1}")


# Dictionary - Dictionary is a mapped data structure. Keys in a dictionary are unique and it is ordered data structure.
my_dictionary = {"andrapradesh" : "amaravathi", "karnataka" : "bangalore", "goa" : "panaji", "tamilanadu" : "chennai", "kerala" : "tiruvanthapuram"}

# Access value from the dictionary
print(f" Access the value with the key : {my_dictionary["kerala"]}")

# Access all values from the dictionary
print(f" All values in a dictionary : {my_dictionary.values()}")

# Access all keys from the dictionary
print(f" All keys in a dictionary : {my_dictionary.keys()}")

# Access all key, value pairs from the dictionary
for key, value in my_dictionary.items():
    print(f" {key} : {value}")

# Get method - Get method is used to get the value from dictionary using key.
print(f" Get method : {my_dictionary.get("goa")}")

# Pop method - Pop method remove an item from the dictionary with key as an argument.
print(f" Pop method : {my_dictionary.pop("goa")}")

# Popitem method - Popitem method will remove last element from the dictionary.
my_dictionary.popitem()

# Update method - Update method is used to update dictionary with other dictionary
my_dictionary.update({"telangana" : "hydrabad"})
print(f"My dictionary : {my_dictionary}")

# From keys method : From keys method is used to get keys from the dictionary.
keys = dict.fromkeys(my_dictionary)
print(keys)

# Setdefault method : Set default method is used to key,value pair common even though if we won't define in dictionary, if user provide value to that key value will be overridden.
my_dictionary.setdefault("delhi", "new delhi")
print(f"My dictionary : {my_dictionary}")






