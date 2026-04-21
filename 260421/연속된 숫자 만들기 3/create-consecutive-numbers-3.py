a = list(map(int, input().split()))
cnt = 0

while True:
    a.sort()
    if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
        break
    if a[0] + 1 == a[2]:
        a[0] = a[1] + 1
        cnt += 1
    elif a[1] + 1 == a[2]:
        a[2] = a[1] - 1
        cnt += 1
print(cnt)