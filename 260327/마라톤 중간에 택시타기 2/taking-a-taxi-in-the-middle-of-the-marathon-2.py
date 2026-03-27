import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

min_dist = sys.maxsize
dist = 0
for i in range(1, n - 1): # 처음 끝 제외한 점프 가능한 구간
    # 점프 구간 i 번째 제외한 거리
    new_dist = dist + abs(x[i-1] - x[i+1]) + abs(y[i-1] - y[i+1])
    # 점프 구간 이후 거리
    for j in range(i + 2, n):
        new_dist += abs(x[j-1] -x[j]) + abs(y[j-1] -y[j]) 
    min_dist = min(min_dist, new_dist)
    dist += abs(x[i] - x[i-1]) + abs(y[i] - y[i - 1]) 

print(min_dist)
