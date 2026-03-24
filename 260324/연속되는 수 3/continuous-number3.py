N = int(input())
arr = [int(input()) for _ in range(N)]

max_c, count = 0, 0
for i in range(N):
    if i == 0 or arr[i] * arr[i-1] < 0:
        count = 0
    count += 1
    if max_c < count :
        max_c = count
print(max_c)