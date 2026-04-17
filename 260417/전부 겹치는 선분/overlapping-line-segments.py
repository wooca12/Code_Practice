n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)


max_a = max(x1)
min_b = min(x2)

# 시작점 a가 끝점 b보다 뒤에 온다면 선분 겹침  
if max_a <= min_b:
    print('Yes')
else:
    print('No')
# ans = 'No'
# for x in range(min(x1), max(x2) + 1):
#     count = 0
#     for a, b in segments:
#         if a <= x <= b:
#             count += 1
#     if count == n:
#         ans = 'Yes'
#         break
# print(ans)