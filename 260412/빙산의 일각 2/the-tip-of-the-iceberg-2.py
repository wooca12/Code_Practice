n = int(input())
h = [int(input()) for _ in range(n)]

max_count = 0
for k in range(1, max(h) + 1):
    count = 0
    stop = False
    for i in range(n):
        diff = h[i] - k
        if not stop and diff > 0:
            count += 1
            stop = True
        elif stop and diff <= 0:
            stop = False
    max_count = max(max_count, count)

print(max_count)
        