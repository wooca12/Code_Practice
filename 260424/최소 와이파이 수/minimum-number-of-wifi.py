import math
n, m = map(int, input().split())
arr = list(map(int, input().split()))

num = n / (m * 2 + 1)
num = math.ceil(num)
print(num)
    
