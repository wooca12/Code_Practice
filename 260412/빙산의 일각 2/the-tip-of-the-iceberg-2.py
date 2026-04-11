n = int(input())
h = [int(input()) for _ in range(n)]

max_count = 0
for k in range(1, max(h) + 1):
    count = 0
    flag = True
    for i in range(1, n):
        if flag and k < h[i]:
            count += 1
            flag = False
        elif k >= h[i]:
            flag = True
    max_count = max(max_count, count)


print(max_count)
        