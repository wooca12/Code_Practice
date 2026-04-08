import sys
N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

min_cost = sys.maxsize

for i in range(N - T + 1):
    for j in range(i + T, N + 1):
        cost = 0
        for k in range(i, j):
            if arr[k] != H:
                cost += abs(H - arr[k])
        min_cost = min(min_cost, cost)
print(min_cost)