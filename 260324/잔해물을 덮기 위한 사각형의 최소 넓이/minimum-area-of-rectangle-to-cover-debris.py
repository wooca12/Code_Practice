
# Please write your code here.
OFFSET = 10
MAX = 2 * OFFSET
blocks = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for n in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            blocks[i][j] = n + 1

area = 0
min_x, min_y = 2 * OFFSET, 2 * OFFSET
max_x, max_y = -2 * OFFSET, -2 * OFFSET

for i in range(MAX + 1):
    for j in range(MAX + 1):
        if blocks[i][j] == 1:
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)

size = (max_x - min_x + 1) * (max_y - min_y + 1)
print(size)
