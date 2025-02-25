def binary_search(input_list, target):
    n = len(input_list)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if input_list[mid] < target:
            l = mid + 1
        elif input_list[mid] > target:
            r = mid - 1
        else:
            return f"Element found at the index of {mid}"
    return "Element not found"

my_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_input, 7))