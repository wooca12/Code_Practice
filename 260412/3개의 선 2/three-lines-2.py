n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)
xs, ys = list(set(x)), list(set(y))
xs.sort(), ys.sort()


ans = 0
for x1 in xs:
    for x2 in xs:
        if x1 == x2:
            continue
        for y in ys:
            count = 0
            for p1, p2 in points:
                if p1 == x1 or p1 == x2 or p2 == y :
                    count += 1
            if count == n:
                ans = 1
                break

for y1 in ys:
    for y2 in ys:
        if y1 == y2:
            continue
        for x in xs:
            count = 0
            for p1, p2 in points:
                if p1 == x or p2 == y1 or p2 == y2 :
                    count += 1
            if count == n:
                ans = 1
                break

print(ans)
    
            


