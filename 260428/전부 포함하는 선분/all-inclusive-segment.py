import sys
INIT_MIN = sys.maxsize
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

a, b = [], []
for x, y in segments:
    a.append(x)
    b.append(y)

ans = INIT_MIN


# Case 1: 맨 앞의 선분 지울 때
skip = 0
for i in range(n):
    if a[skip] > a[i]:
        skip = i

min_a, max_b = INIT_MIN, -INIT_MIN
for i in range(n):
    if i == skip:
        continue
    min_a = min(min_a, a[i])
    max_b = max(max_b, b[i])

ans = min(ans, max_b - min_a)

# Case 2: 맨 뒤의 선분 지울 때
skip = 0
for i in range(n):
    if b[skip] < b[i]:
        skip = i

min_a, max_b = INIT_MIN, -INIT_MIN
for i in range(n):
    if i == skip:
        continue
    min_a = min(min_a, a[i])
    max_b = max(max_b, b[i])
ans = min(ans, max_b - min_a)

print(ans)



# min_length = INIT_MIN

# for i in range(n):
#     min_a, max_b = INIT_MIN, -INIT_MIN
#     for j in range(n):
#         if i == j:
#             continue
#         min_a = min(min_a, segments[j][0])
#         max_b = max(max_b, segments[j][1])
#     min_length = min(min_length, max_b - min_a)

# print(min_length)
        
    
