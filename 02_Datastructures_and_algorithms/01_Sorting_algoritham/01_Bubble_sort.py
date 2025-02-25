def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

my_input = [7, 2, 9, 0, 1, 6, 4, 8, 5, 3]
print(f"Bubble sort : {bubble_sort(my_input)}")