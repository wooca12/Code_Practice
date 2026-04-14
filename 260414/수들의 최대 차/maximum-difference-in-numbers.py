N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

max_count = 0
for i in range(1, 10001):
    count = 0
    for num in arr:
        if i <= num and num <= i + K:
            count += 1
    max_count = max(max_count, count)
print(max_count)
