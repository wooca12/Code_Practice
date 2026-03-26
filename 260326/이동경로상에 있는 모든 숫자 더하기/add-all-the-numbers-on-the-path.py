N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

x, y = N//2, N // 2
d = 3
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
sum = board[x][y]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for c in str:
    if c == 'L':
        d = (d - 1 + 4) % 4
    elif c == 'R':
        d = (d + 1) % 4
    elif c == 'F':
        nx, ny = x + dx[d], y + dy[d]
        if not in_range(nx, ny):
            continue
        x, y = x + dx[d], y + dy[d]
        sum += board[x][y]
print(sum)

