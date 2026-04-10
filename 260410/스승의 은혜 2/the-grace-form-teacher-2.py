N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

max_count = 0
P.sort()

for i in range(N):
    price = P[i] // 2
    if price > B:
        continue
    count = 1
    for j in range(N):
        if i == j: 
            continue
        price += P[j]
        if price > B:
            continue
        count += 1
    max_count = max(max_count, count)
print(max_count)