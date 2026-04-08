N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

arr = [0] * 401

for i in range(N) :
    arr[pos[i] + 200] += candy[i]


max_num = 0
for i in range(1, 401 - 2*K):
    sum = 0
    for j in range(i, i + 2*K + 1):
        sum += arr[j]
    max_num = max(max_num, sum)

print(max_num)
