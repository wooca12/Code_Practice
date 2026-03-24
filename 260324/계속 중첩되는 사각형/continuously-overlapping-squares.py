n = int(input())
count_r, count_b = 0, 0

OFFSET = 100
MAX = 2 * OFFSET
blocks = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    for x in range(a, c):
        for y in range(b, d):
            if i % 2 == 0:
                blocks[x][y] = 1
            else:
                blocks[x][y] = 2

area = 0
for i in range(MAX + 1):
    for j in range(MAX + 1):
        if blocks[i][j] == 2:
            area += 1
print(area) 