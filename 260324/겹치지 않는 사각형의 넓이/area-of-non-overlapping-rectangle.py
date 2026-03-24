
x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())


OFFSET = 1000
MAX = 2 * OFFSET
blocks = [[0] * (MAX + 1) for i in range(MAX + 1)]
for i in range(2):
    for a in range(x1[i], x2[i]):
        for b in range(y1[i], y2[i]):
            blocks[a][b] = 1
for a in range(x1[2], x2[2]):
    for b in range(y1[2], y2[2]):
        blocks[a][b] = 0

size = 0
for i in range(MAX + 1):
    for j in range(MAX + 1):
        if blocks[i][j] == 1:
            size += 1
print(size)
