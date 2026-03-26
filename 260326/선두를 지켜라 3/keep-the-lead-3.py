N, M = map(int, input().split())
a_movements = [0]
for _ in range(N):
    vi, ti = map(int, input().split())
    for t in range(ti):
        a_movements.append(a_movements[-1] + vi)

b_movements = [0]
for _ in range(M):
    vi, ti = map(int, input().split())
    for t in range(ti):
        b_movements.append(b_movements[-1] + vi)



a_i, b_i = 0, 0
first = [0]
count = 0

for i in range(1, max(len(a_movements), len(b_movements))):
    a_i = i if i < len(a_movements) else a_i
    b_i = i if i < len(b_movements) else b_i

    if a_movements[a_i] == b_movements[b_i] and [1, 2] != first:
        first = [1, 2]
        count += 1
    elif a_movements[a_i] > b_movements[b_i] and [1] != first:
        first = [1]
        count += 1
    elif a_movements[a_i] < b_movements[b_i] and [2] != first:
        first = [2]
        count += 1
print(count)