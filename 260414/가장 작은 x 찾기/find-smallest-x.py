n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

min_x = 10001


for x in range(1, 10001):
    success = True
    num  = x
    for i in range(n):
        num *= 2
        if a[i] > num or num > b[i]:
            success = False
            break
    if success:
        min_x = x
        break
            
print(min_x)
