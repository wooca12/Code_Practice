n = int(input())
arr = [int(input()) for _ in range(n)]

count, max_c = 0, 0
for i in range(n):
    if i != 0 and arr[i - 1] >= arr[i]:
        count = 0
    count += 1
    max_c = max(max_c, count)
print(max_c)