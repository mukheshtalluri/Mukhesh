# Native recursion
def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 2) + fib_recursive(n - 1)

print(fib_recursive(7))

# Top down DP - Memoization
def fib_memoization(n):
    memo = {0 : 0, 1 : 1}
    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x - 2) + f(x - 1)
            return memo[x]
    return f(n)

print(fib_memoization(7))

# Bottom up DP - Tabulation
def fib_tabulation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]

print(fib_tabulation(7))

# Constant space
def fib_constant(n):
    if n == 0:
        return n
    if n == 1:
        return 1
    prev = 0
    cur = 1
    for i in range(2, n + 1):
        prev, cur = cur, prev + cur

    return cur

print(fib_constant(7))