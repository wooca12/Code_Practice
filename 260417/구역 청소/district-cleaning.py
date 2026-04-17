a, b = map(int, input().split())
c, d = map(int, input().split())


def intersecting(x1, x2, x3, x4):
    if x2 < x3 or x4 < x1:
        return False
    else:
        return True

if intersecting(a,b,c,d):
    print(max(b, d) - min(a, c))
else:
    print((b-a) + (d-c))

# # 안겹칠때
# if d <= a or b <= c:
#     area = abs(b - a) + abs(d - c)
# # 겹칠때 1. B구역이 A 구역에 포함
# elif (a < c < d < b) :
#     area = abs(b - a)
# elif (c < a < b < d):
#     area = abs(d - c)
# # 겹칠때 2. 걸쳐 있을때 
# elif a < c < b < d :
#     area = abs(b - a) + abs(d - b)
# elif c < a < d < b : 
#     area = abs(b - a) + abs(a - c)
# else:
#     area = abs(b - a)
# print(area)