x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

c1 = min(x1, a1)
d1 = min(y1, b1)
c2 = max(x2, a2)
d2 = max(y2, b2)


f = max(c2 - c1, d2 - d1)
size = f * f

print(size)