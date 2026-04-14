n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]


max_count = 0
for a, b in pairs:
    count = 0
    for x, y in pairs:
        if a == x and b == y or a == y and b == x:
            count += 1
    max_count = max(max_count, count)
print(max_count)
        