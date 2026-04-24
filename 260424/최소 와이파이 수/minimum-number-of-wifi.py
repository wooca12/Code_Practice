import math
n, m = map(int, input().split())
arr = list(map(int, input().split()))

if m == 0:
    num = sum(arr)
else:
    num = n / (m * 2 + 1)
    num = math.ceil(num)
print(num)
    
