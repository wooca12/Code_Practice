n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

OFFSET = 100
MAX = 2 * OFFSET

blocks = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for x1, y1 in points:
    for i in range(x1, x1 + 8):
        for j in range(y1, y1 + 8):
            blocks[i][j] = 1

area = 0
for i in range(MAX + 1):
    for j in range(MAX + 1):
        if blocks[i][j] == 1:
            area += 1
print(area)