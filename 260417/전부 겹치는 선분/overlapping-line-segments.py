n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

ans = 'No'
for x in range(min(x1), max(x2) + 1):
    count = 0
    for a, b in segments:
        if a <= x <= b:
            count += 1
    if count == n:
        ans = 'Yes'
        break
print(ans)