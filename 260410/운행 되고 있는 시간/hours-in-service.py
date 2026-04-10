n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

max_time = 0

for i in range(n):
    count = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        x1, x2 = a[j], b[j]
        for k in range(x1, x2):
            count[k] = 1
    max_time = max(max_time, sum(count))
print(max_time)