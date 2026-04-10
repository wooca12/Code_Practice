n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

max_size = 0

def get_size(x1, y1, x2, y2, x3, y3):
    return abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))

    return w * h

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if (x1 == x2 or x2 == x3 or x1 == x3) and (y1 == y2 or y2 == y3 or y1 == y3):
                max_size = max(max_size, get_size(x1, y1, x2, y2, x3, y3))
print(max_size)