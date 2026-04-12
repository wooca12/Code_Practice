N = int(input())
seat = [int(i) for i in list(input())]

max_dist = 0
use_seat = [i for i in range(N) if seat[i] != 0]

for i in range(N): # 모든 좌석 순회함
    if seat[i] == 1: # 이미 좌석 차지한 경우 뺌
        continue
    uses = [i for i in use_seat]
    uses.append(i)
    uses.sort()
    dist = N
    for j in range(len(uses) - 1):
        dist = min(dist, uses[j+1] - uses[j])
    max_dist = max(max_dist, dist)

print(max_dist)

        


    