import sys
n = int(input())
a = [0] + list(map(int, input().split()))

min_n = min(a[1:])
min_diff = sys.maxsize
ans = -1

for i in range(1, n+1):
    if a[i] == min_n:
        continue
    # 최소 간격 2개 이상
    elif a[i] - min_n == min_diff:
        ans = -1
        break
    elif a[i] - min_n < min_diff:
        ans = i
        min_diff = a[i] - min_n
print(ans)