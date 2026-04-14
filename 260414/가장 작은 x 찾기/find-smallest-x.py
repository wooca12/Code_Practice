n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

min_x = 10


for x in range(1, 11):
    success = True
    num  = x
    for i in range(n):
        num *= 2
        if a[i] > num or num > b[i]:
            success = False
    if success:
        min_x = min(min_x, x)
            
print(min_x)
