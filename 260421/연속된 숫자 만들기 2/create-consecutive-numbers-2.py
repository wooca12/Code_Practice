pos = list(map(int, input().split()))

def correct(pos):
    if pos[1] - pos[0] == 1 and pos[2] - pos[1] ==1 :
        return True
    return False

cnt = 0
while True:
    pos.sort()
    if correct(pos):
        break
    # 1번째 이동
    if pos[2] - 1 not in pos:
        pos[0] = pos[2] - 1
        cnt += 1
    elif pos[0] + 1 not in pos:
        pos[2] = pos[0] + 1
        cnt += 1
print(cnt)