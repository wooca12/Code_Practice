n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#    우  하  좌  상
dxs = [0, 1]
dys = [1, 0]

max_count = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(n):
    for j in range(2, n):
        count1 = arr[i][j-2] + arr[i][j-1] + arr[i][j]
        for dx, dy in zip(dxs, dys):
            curx, cury = i, j
            while True:
                nx, ny = curx + dx, cury + dy
                if not in_range(nx, ny):
                    break
                count2 = arr[nx][ny-2] + arr[nx][ny-1] + arr[nx][ny]
                max_count = max(max_count, count1 + count2)
                curx, cury = nx, ny
print(max_count)