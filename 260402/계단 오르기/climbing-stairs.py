N = int(input())

memo = [-1] * 1001

def solution(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 1:
        memo[n] = 0
    elif 2 <= n <= 3:
        memo[n] = 1
    else:
        memo[n] = solution(n-2) + solution(n-3)
    return memo[n]

print(solution(N) % 10007)
