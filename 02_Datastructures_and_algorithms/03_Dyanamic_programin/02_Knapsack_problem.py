# Native recursion
def knapsack_recursion(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack_recursion(weights, values, capacity, n - 1)

    pick = values[n - 1] + knapsack_recursion(weights, values, capacity - weights[n - 1], n - 1)
    skip = knapsack_recursion(weights, values, capacity, n - 1)
    return max(pick, skip)

weights = [2, 5, 7, 9]
values = [2, 3, 4, 7]
capacity = 1
n = len(weights)
print(f"Maximum value : {knapsack_recursion(weights, values, capacity, n)}")

# Top down DP - Memoization
