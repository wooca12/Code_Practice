pos = list(map(int, input().split()))
pos.sort()
ans = 0
if pos[0] + 1 == pos[1] and pos[1] + 1 == pos[2]:
    ans = 0
elif pos[0] + 1 == pos[1] or pos[1] + 1 == pos[2]:
    ans = 1
elif pos[0] + 2 == pos[1] or pos[1] + 2 == pos[2]:
    ans = 1
else:
    ans = 2
print(ans)