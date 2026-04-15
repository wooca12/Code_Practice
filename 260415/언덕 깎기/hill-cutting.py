import sys
N = int(input())
heights = [int(input()) for _ in range(N)]
k = 17

MAX_H = 100
mincost = sys.maxsize

# 크기가 17이 되는 모든 구간 잡기
# 구간 안데 들어오게 언덕을 깍음
for i in range(MAX_H):
    # [i, i + 17] 구간에서 언덕을 깍는 비용 계산
    # i + 17보다 높을때 : 언덕이 i + 17되도록 깎음
    # i보다 낮을때 : 언덕이 i가 되도록 쌓음
    cost = 0
    for j in range(N):
        if heights[j] < i:
            cost += (i - heights[j]) ** 2
        if heights[j] > i + 17:
            cost += (i + k - heights[j]) ** 2
    mincost = min(mincost, cost)
print(mincost)
        
        
    
