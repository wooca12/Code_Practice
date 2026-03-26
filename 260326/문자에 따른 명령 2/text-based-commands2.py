dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dirs = input()
x, y, = 0, 0
d = 3
for i in dirs:
    if i == 'L':
        d = (d - 1 + 4) % 4
    elif i == 'R':
        d = (d + 1) % 4
    elif i == 'F':
        x += dx[d]
        y += dy[d]
print(x, y)