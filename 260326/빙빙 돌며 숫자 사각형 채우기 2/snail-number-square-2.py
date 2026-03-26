n, m = map(int, input().split())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
d = 1

arr = [[0] * m for _ in range(n)]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(1, n * m + 1):
    arr[x][y] = i
    nx, ny = x + dx[d], y + dy[d]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        d = (d - 1 + 4) % 4
    x, y = x + dx[d], y + dy[d]


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
