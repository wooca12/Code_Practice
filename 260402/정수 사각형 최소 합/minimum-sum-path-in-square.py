# N×N 행렬이 주어졌을 때, (1, N)에서 시작하여 왼쪽 혹은 밑으로만 이동하여 (N, 1)로 간다고 했을 때 거쳐간 위치에 적혀있는 숫자의 합을 최소로 하는 프로그램을 작성해보세요.
import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def initialize(dp):
    dp[0][n-1] = grid[0][n-1]

    # 왼쪽 이동
    for i in range(1, n):
        dp[0][n-i-1] = dp[0][n-i] + grid[0][n-i-1]

    #아래 이동
    for i in range(1, n):
        dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1]

    return dp

def undate(dp):
    for i in range(1, n):
        for j in range(n-2, -1, -1):
            dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j+1] + grid[i][j])
    return dp

dp = initialize(dp)
dp = undate(dp)

print(dp[n-1][0])


