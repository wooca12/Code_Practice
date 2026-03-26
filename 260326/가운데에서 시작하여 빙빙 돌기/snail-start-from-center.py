n = int(input())
grid = [[0] * n for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = n // 2, n // 2
d = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(1, n * n + 1):
    grid[x][y] = i
    nd = (d - 1 + 4) % 4
    nx, ny = x + dx[nd], y + dy[nd]
    if in_range(nx, ny) and grid[nx][ny] == 0:
        d = (d - 1 + 4) % 4
    x, y = x + dx[d], y + dy[d]


for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
