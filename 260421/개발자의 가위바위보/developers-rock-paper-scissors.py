N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]

maxcnt = 0
win = 0
for a, b in moves:
    if a == 1 and b == 2:
        win += 1
    elif a == 2 and b == 3:
        win += 1
    elif a == 3 and b == 1:
        win += 1
maxcnt = max(maxcnt, win)

win = 0
for a, b in moves:
    if a == 1 and b == 3:
        win += 1
    elif a == 2 and b == 1:
        win += 1
    elif a == 3 and b == 2:
        win += 1
maxcnt = max(maxcnt, win)

print(maxcnt)