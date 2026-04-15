N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

max_count = 0
for i in range(N):
    count = 0
    for j in range(i+1, N):
        if num[i] == num[j] and j - i <= N:
            count += 1
    max_count = max(max_count, count)
print(max_count)
