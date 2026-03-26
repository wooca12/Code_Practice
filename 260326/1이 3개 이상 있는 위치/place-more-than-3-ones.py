n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y and y < n

area = 0
for i in range(n):
    for j in range(n):
        count = 0
        for dx, dy, in zip(dxs, dys):
            x = i + dx
            y = j + dy
            if in_range(x, y) and grid[x][y] == 1:
                count += 1

        if count > 2:
            area += 1
print(area)