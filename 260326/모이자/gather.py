import sys
n = int(input())
A = list(map(int, input().split()))

min_sum = sys.maxsize
for mid in range(n):
    sum_diff = 0
    for j in range(n):
        sum_diff += A[j] * abs(mid - j)
    min_sum = min(min_sum, sum_diff)
print(min_sum)
