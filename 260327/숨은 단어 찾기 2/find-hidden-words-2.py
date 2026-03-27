N, M = map(int, input().split())
arr = [input() for _ in range(N)]


# 3 4 5
# 6 c 7
# 0 1 2
dxs = [1, 1, 1, -1, -1, -1, 0, 0]
dys = [-1, 0, 1, -1, 0, 1, -1, 1]
LEE = 'LEE'

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

number = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != LEE[0]:
            continue
        for dx, dy in zip(dxs, dys):
            chr_idx = 1
            cur_x, cur_y = i, j
            while True:
                nx, ny = cur_x + dx, cur_y + dy
                if not in_range(nx, ny):
                    break
                if arr[nx][ny] != LEE[chr_idx]:
                    break
                cur_x, cur_y = nx, ny
                chr_idx += 1
                if chr_idx == 3:
                    number += 1
                    break

print(number)
