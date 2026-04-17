a, b = map(int, input().split())
c, d = map(int, input().split())

# 안겹칠때
if d < a or b < c:
    area = abs(b - a) + abs(d - c)
# 겹칠때 1. B구역이 A 구역에 포함
elif (a < c and d < b) or (c < a and b < d):
    area = abs((b - a) - (d - c))
# 겹칠때 2. 걸쳐 있을때 
elif a < c < b < d :
    area = abs(b - a) + abs(d - b)
elif c < a < d < b : 
    area = abs(b - a) + abs(a - c)

print(area)