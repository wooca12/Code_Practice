import sys

#(0,-1), (-1, -1), (-1, 0), (-1, 1), (0, 1)
#_ \ | / _
#   / | \
# (1, -1), (1, 0), (1, 1)


# 변수 선언 및 입력
arr = [
    list(map(int, input().split()))
    for _ in range(19)
]
dxs = [1, 1, 1, -1, -1, -1, 0, 0]
dys = [-1, 0, 1, -1, 0, 1, -1, 1]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

for i in range(19):
    for j in range(19):
        if arr[i][j] == 0:
            continue

        for dx, dy in zip(dxs, dys):
            cur_t = 1
            cur_x = i
            cur_y = j
            while True:
                nx = cur_x + dx
                ny = cur_y + dy
                if not in_range(nx, ny):
                    break
                if arr[nx][ny] != arr[i][j]:
                    break
                cur_t += 1
                cur_x = nx
                cur_y = ny

                if cur_t == 5:
                    print(arr[i][j])
                    print(i + dx * 2 + 1, j + dy * 2 + 1)
                    sys.exit()
print(0)
