a = list(map(int, input().split()))
cnt = max(a[1] - a[0], a[2] - a[1]) - 1

print(cnt)