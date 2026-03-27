import sys
n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = sys.maxsize
total_sum = sum(arr)

for i in range(n-1):
    for j in range(i, n):
        sum = total_sum - (arr[i] + arr[j])
        min_diff = min(min_diff, abs(sum - s))
print(min_diff)



