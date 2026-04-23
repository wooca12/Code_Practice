import sys
n = int(input())
a = [0] + list(map(int, input().split()))

min_n = min(a[1:])
min_diff = sys.maxsize
ans = -1
cnt = 0

for i in range(1, n+1):
    if a[i] == min_n:
        continue
    # 더 간격이 작은 숫자 등장 시
    elif a[i] - min_n < min_diff:
        ans = i
        cnt = 1
        min_diff = a[i] - min_n
    # 간격이 똑같은 숫자 등장 시
    elif a[i] - min_n == min_diff:
        cnt += 1


# 등장 횟수 0 또는 2 이상
if cnt == 0 or cnt > 1:
    print(-1)
else:
    print(ans)