def merge_sort(input_list):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        left_part = input_list[:mid]
        right_part = input_list[mid:]

        merge_sort(left_part)
        merge_sort(right_part)

        i = 0
        j = 0
        k = 0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                input_list[k] = left_part[i]
                i += 1
            else:
                input_list[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            input_list[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            input_list[k] = right_part[j]
            j += 1
            k += 1

    return input_list

my_input = [7, 2, 9, 0, 1, 6, 4, 8, 5, 3]
sorted_list = merge_sort(my_input)
print(f"Merge sort : {sorted_list}")