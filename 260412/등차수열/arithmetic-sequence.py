n = int(input())
a = list(map(int, input().split()))

max_count = 0


for k in range(min(a), max(a) + 1):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            if k - a[i] == a[j] - k:
                count += 1

    max_count = max(max_count, count)
print(max_count)