n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

lines = []
for i in set(x):
    lines.append([i, 0])
for i in set(y):
    lines.append([0, i])

ln = len(lines)
ans = 0
for i in range(ln):
    for j in range(i + 1, ln):
        for k in range(j + 1, ln):
            for x, y in points:
                l = [lines[i], lines[j], lines[k]]
                xs, ys = zip(*l)
                xs, ys = list(xs), list(ys)
                if x in xs or y in ys:
                    ans = 1
                    break
print(ans)

