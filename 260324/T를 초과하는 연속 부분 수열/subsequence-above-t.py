n, t = map(int, input().split())
arr = list(map(int, input().split()))

count, max_c = 0, 0

for i in range(n):
    if arr[i] > t and arr[i] > arr[i - 1]:
        count += 1
    elif arr[i] <= t:
        count = 0
    else:
        count = 1
    max_c = max(max_c, count)
print(max_c)