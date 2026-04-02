n = int(input())

memo = [-1] * 20

def solve(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 1:
        memo[n] = 1
    else:
        memo[n] = 0
        for i in range(0, n):
            memo[n] = memo[n] + solve(i) * solve(n - i - 1)
    return memo[n]

print(solve(n))

