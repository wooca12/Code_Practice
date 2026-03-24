n, t = map(int, input().split())
arr = list(map(int, input().split()))

count, max_c = 0, 0

for i in range(n):
    if arr[i] > t :
        count += 1
    elif arr[i] <= t:
        count = 0
    max_c = max(max_c, count)
print(max_c)