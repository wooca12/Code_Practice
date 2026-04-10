n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

max_size = 0

def get_size(i1, i2, i3):
    w, h = 0, 0
    # x 축에 평행 --> y값 같음
    if y[i1] == y[i2]:
        w = abs(x[i1] - x[i2])
    elif y[i1] == y[i3]:
        w = abs(x[i1]- x[i3])
    elif y[i2] == y[i3]:
        w = abs(x[i2] - x[i3])
    # y 축에 평행 --> x값 같음
    if x[i1] == x[i2]:
        h = abs(y[i1] - y[i2])
    elif x[i1] == x[i3]:
        h = abs(y[i1]-y[i3])
    elif x[i2] == x[i3]:
        h = abs(y[i2] - y[i3])
    return w * h

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i == j or j == k or i == k:
                continue
            size = get_size(i, j, k)
            max_size = max(max_size, size)
print(max_size)