import sys
INIT_MIN = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_diff = INIT_MIN
for i in range(n):
    min_diff = min(min_diff, abs(arr[i] - arr[i+n]))
print(min_diff)