def selection_sort(input_list):
    n = len(input_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if input_list[j] > input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list

my_input = [7, 2, 9, 0, 1, 6, 4, 8, 5, 3]
print(f"Selection sort : {selection_sort(my_input)}")