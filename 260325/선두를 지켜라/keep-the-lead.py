from binascii import a2b_base64

n, m = map(int, input().split())

# Process A's movements
a_moves = []
b_moves = []
for _ in range(n):
    a_moves.append(map(int, input().split()))

for _ in range(m):
    b_moves.append(map(int, input().split()))

a_dis = [0]
for v, times in a_moves:
    for t in range(1, times + 1):
        dis = a_dis[-1] + v
        a_dis.append(dis)

b_dis = [0]
for v, times in b_moves:
    for t in range(1, times + 1):
        dis = b_dis[-1] + v
        b_dis.append(dis)

first, count = 0, 0

for i in range(len(a_dis)):
    if first == 0:
        first = 1 if a_dis[i] < b_dis[i] else 2
    elif first == 1 and a_dis[i] < b_dis[i]:
        first = 2
        count += 1
    elif first == 2 and a_dis[i] > b_dis[i]:
        first = 1
        count += 1
print(count)