n = int(input())
arr = [int(input()) for _ in range(n)]

count, max_count =  0, 0
for i in range(n):
    count += 1
    if i == 0 or arr[i] != arr[i - 1]:
        count = 1
    if max_count < count:
        max_count = count

print(max_count)