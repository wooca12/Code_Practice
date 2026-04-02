
n = int(input())

memo = [-1] * 1001

def solve(n):
    if memo[n] != -1:
        return memo[n]
    if n < 0:
        memo[n] = 0
    elif n == 0:
        memo[n] = 1
    elif n == 1:
        memo[n] = 2
    else:
        memo[n] = 2 * solve(n-1) + 3 * solve(n-2)
        for i in range(n-3, -1, -1):
            memo[n] = memo[n] + 2 * solve(i)

    return memo[n]

print(solve(n) % 1000000007)
