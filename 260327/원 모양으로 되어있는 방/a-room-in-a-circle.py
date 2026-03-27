import sys
n = int(input())
a = [int(input()) for _ in range(n)]

min_dist = sys.maxsize
for i in range(n): # i 시작 방
    dist = 0
    for j in range(n):
        d = (i + j) % n # 사람마다 가야할 거리
        dist += a[j] * d
    min_dist = min(min_dist, dist)

print(min_dist)