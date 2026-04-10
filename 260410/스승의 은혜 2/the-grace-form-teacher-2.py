N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

max_count = 0
P.sort()

for i in range(N):
    tmp = [P[j] for j in range(N)]
    tmp[i] /= 2

    count, price = 0, 0
    for j in range(N):
        if price + tmp[j] > B:
            break
        price += tmp[j]
        count += 1
    max_count = max(max_count, count)
print(max_count)