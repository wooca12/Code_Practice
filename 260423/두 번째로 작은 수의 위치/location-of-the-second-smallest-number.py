import sys
n = int(input())
a = list(map(int, input().split()))


sorted_arr = sorted(a)
exist = False
low2 = 0

for i in range(n):
    if sorted_arr[i] != sorted_arr[0]:
        exist = True
        low2 = sorted_arr[i]
        break
        
if not exist:
    print(-1)
    sys.exit()

ans = -1
for i in range(n):
    if a[i] == low2:
        if ans != -1:
            print(-1)
            sys.exit()
        ans = i

print(ans + 1)

# min_n = min(a[1:])
# min_diff = sys.maxsize
# ans = -1
# cnt = 0

# for i in range(1, n+1):
#     if a[i] == min_n:
#         continue
#     # 더 간격이 작은 숫자 등장 시
#     elif a[i] - min_n < min_diff:
#         ans = i
#         cnt = 1
#         min_diff = a[i] - min_n
#     # 간격이 똑같은 숫자 등장 시
#     elif a[i] - min_n == min_diff:
#         cnt += 1


# # 등장 횟수 0 또는 2 이상
# if cnt == 0 or cnt > 1:
#     print(-1)
# else:
#     print(ans)