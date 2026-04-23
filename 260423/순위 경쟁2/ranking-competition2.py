n = int(input())
arr = []
for _ in range(n):
    ci, si = input().split()
    arr.append((ci, int(si)))

cnt = 0
win = ['A', 'B']
a, b = 0, 0
for p, s in arr:
    if p == 'A':
        a += s
    elif p == 'B':
        b += s
    if a > b and win != ['A']:
        win = ['A']
        cnt += 1
    elif a < b and win != ['B']:
        win = ['B']
        cnt += 1
    elif a == b and win != ['A', 'B']:
        win = ['A', 'B']
        cnt += 1
print(cnt)
    