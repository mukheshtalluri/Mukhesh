def insertion_sort(input_list):
    n = len(input_list)
    for i in range(1, n):
        key = input_list[i]
        j = i - 1
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key
    return input_list

my_input = [7, 2, 9, 0, 1, 6, 4, 8, 5, 3]
print(f"Insertion sort : {insertion_sort(my_input)}")