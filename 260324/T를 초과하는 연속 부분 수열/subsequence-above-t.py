n, t = map(int, input().split())
arr = list(map(int, input().split()))

count, max_c = 0, 0

for i in range(n):
    if i == 0 or arr[i] - arr[i-1] == 1 and arr[i] > t:
        count += 1
    else:
        count = 1
    max_c = max(max_c, count)
print(max_c)