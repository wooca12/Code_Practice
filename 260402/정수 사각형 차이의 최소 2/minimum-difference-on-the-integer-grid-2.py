import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_dp = [[-sys.maxsize] * n for _ in range(n)]
min_dp = [[sys.maxsize] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def print_all(arr):
    print()
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


def initialize():
    max_dp[0][0], min_dp[0][0] = grid[0][0], grid[0][0]
    dp[0][0] = grid[0][0]
    # 아래
    for i in range(1, n):
        max_dp[i][0] = max(max_dp[i - 1][0], grid[i][0])
        min_dp[i][0] = min(min_dp[i - 1][0], grid[i][0])
        dp[i][0] =  max_dp[i][0] - min_dp[i][0]
    # 오른쪽
    for i in range(1, n):
        max_dp[0][i] = max(max_dp[0][i - 1], grid[0][i])
        min_dp[0][i] = min(min_dp[0][i - 1], grid[0][i])
        dp[0][i] = max_dp[0][i] - min_dp[0][i]

def update():
    for i in range(1, n):
        for j in range(1, n):
            up_max = max(max_dp[i - 1][j], grid[i][j])
            up_min = min(min_dp[i - 1][j], grid[i][j])
            left_max = max(max_dp[i][j - 1], grid[i][j])
            left_min = min(min_dp[i][j - 1], grid[i][j])

            max_dp[i][j] = min(up_max, left_max)
            min_dp[i][j] = max(up_min, left_min)

            dp[i][j] = max_dp[i][j] - min_dp[i][j]


initialize()
update()
# print_all(max_dp)
# print_all(min_dp)
# print_all(dp)

print(dp[n - 1][n - 1])
