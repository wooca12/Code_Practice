import sys
N = int(input())
heights = [int(input()) for _ in range(N)]

MAX_H = 100
mincost = sys.maxsize

min_h = min(heights)
max_h = max(heights)

for i in range(1, 100):
    for j in range(1, 100):
        diff = (max_h - j) - (min_h + i)
        if  0 <= diff <= 17:
            cost = i*i + j*j
            mincost = min(mincost, cost)
print(mincost)
        
    
