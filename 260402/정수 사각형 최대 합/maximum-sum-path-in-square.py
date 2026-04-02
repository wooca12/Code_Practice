import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = -sys.maxsize
dp = [[0] * n for i in range(n)]

def initialize(dp):
    dp[0][0] = grid[0][0]

    # 아래 이동
    for i in range(1, n):
       dp[i][0] = dp[i - 1][0] + grid[i][0]
    # 오른쪽 이동
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    return dp

def update(dp):
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
    return dp

dp = initialize(dp)
dp = update(dp)
for i in range(n):
    for j in range(n):
        answer = max(answer, dp[i][j])
   #      print(dp[i][j], end=' ')
   #  print()

print(answer)
