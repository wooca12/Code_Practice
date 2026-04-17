import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX = 10000

mincost = sys.maxsize

for i in range(1, MAX):
    cost = 0
    for j in range(n):
        # 구간 [i, i+k] 안에 안들어오면 숫자 벼시킴
        if  arr[j] < i:
            cost += abs(arr[j] - i)
        elif arr[j] > i + k:
            cost += abs(arr[j] - i - k)
    mincost = min(mincost, cost)

print(mincost)

