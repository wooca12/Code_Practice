import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

lines = set()
for i in set(x):
    lines.add((i, 0))
for i in set(y):
    lines.add((0, i))
lines = list(lines)
ln = len(lines)

for i in range(ln):
    for j in range(i + 1, ln):
        for k in range(j + 1, ln):
            ans = 1
            for x, y in points:
                l = [lines[i], lines[j], lines[k]]
                xs, ys = zip(*l)
                xs, ys = list(xs), list(ys)
                if x not in xs and y not in ys:
                    ans = 0
                    break
            if ans:
                print(ans)
                sys.exit()
print(ans)
    
