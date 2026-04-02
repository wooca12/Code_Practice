import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]
#    우  하  왼  상
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

cells = []
def init_cell():
    for i in range(n):
        for j in range(n):
            cells.append((grid[i][j], i, j))
    cells.sort()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

init_cell()

for num, x, y in cells:
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

ans = -sys.maxsize
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])
print(ans)
