n = int(input())

memo = [-1] * 1001

def solve(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 1:
        memo[n] = 1
    else:
        memo[n] = solve(n-1) + solve(n-2) + solve(n-2)
    return memo[n]

print(solve(n) % 10007)