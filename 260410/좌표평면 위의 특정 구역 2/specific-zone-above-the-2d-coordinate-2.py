import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_size = sys.maxsize

for i in range(n):
    x1, y1 = 40000, 40000
    x2, y2 = 1, 1
    for j in range(n):
        if i == j:
            continue 
        x1 = min(x1, points[j][0])
        x2 = max(x2, points[j][0])
        y1 = min(y1, points[j][1])
        y2 = max(y2, points[j][1]) 
    size = abs(x1 - x2) * abs(y1 - y2)
    min_size = min(min_size, size)

print(min_size)
