def linear_search(input_list, target):
    for i in range(len(input_list)):
        if input_list[i] == target:
            return f"Element found at the index of {i}"
    return "Element not found."

my_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(my_input, 25))