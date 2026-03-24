OFFSET = 100
blocks = [[0] * (OFFSET*2 + 1) for _ in range(OFFSET*2 + 1)]

n = int(input())
x1, y1, x2, y2 = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a + OFFSET)
    y1.append(b + OFFSET)
    x2.append(c + OFFSET)
    y2.append(d + OFFSET)
\
for i in range(n):
    for a in range(x1[i], x2[i]):
        for b in range(y1[i], y2[i]):
            blocks[a][b] = 1

size = sum(sum(blocks[i])for i in range(OFFSET * 2 + 1))
print(size)

