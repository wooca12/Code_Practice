import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = -sys.maxsize

for i in range(n - k + 1):
    sum = 0
    for j in range(i, i + k):
        sum += arr[j]
    max_sum = max(max_sum, sum)

print(max_sum) 