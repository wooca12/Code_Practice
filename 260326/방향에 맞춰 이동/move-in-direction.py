n = int(input())
movements = []
for i in range(n):
    dir, dist = input().split()
    if dir == 'E':
        dir = 0
    elif dir == 'S':
        dir = 1
    elif dir == 'W':
        dir = 2
    else:
        dir = 3
    movements.append((dir, int(dist)))


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
for d, l in movements:
    x += dx[d] * l
    y += dy[d] * l

print(x, y)
