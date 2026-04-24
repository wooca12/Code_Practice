import math
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 거리가 0 일때 : 사람 사는 곳마다 있어야 함
if m == 0:
    num = sum(arr)

# 사람이 없을 때 : 설치할 필요 없음
elif sum(arr) == 0:
    num = 0
# 거리가 0 이상, 사람 1 이상
else:
    num = n / (m * 2 + 1)
    num = math.ceil(num)
print(num)
    
