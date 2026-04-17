N = int(input())
pigeon_pos = [-1] * 11
moves = []
count = 0
for _ in range(N):
    p, pos = map(int, input().split())
    moves.append((p, pos))

count = 0
for p, pos in moves:
    if pigeon_pos[p] == -1:
        pigeon_pos[p] = pos
    elif pigeon_pos[p] != pos:
        count += 1
print(count)
    

