n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
xs, ys = zip(*points)
xs, ys = list(xs), list(ys)

min_M = 100

def count_points(x, y):
    num_p = [0] * 4
    for p1, p2 in points:
        if p1 < x and p2 < y:
            num_p[0] += 1
        elif p1 < x and p2 > y:
            num_p[1] += 1
        elif p1 > x and p2 < y:
            num_p[2] += 1
        elif p1 > x and p2 > y:
            num_p[3] += 1
    return num_p

for x in range(max(xs) + 1):
    for y in range(max(ys) + 1):
        if x % 2 != 0 or y % 2 != 0:
            continue
        num_points = count_points(x, y)
        min_M = min(min_M, max(num_points))
print(min_M)

