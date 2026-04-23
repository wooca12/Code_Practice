N = int(input())
seats = list(input())

max_cnt = 0
max_i, max_j = 0, 0
for i in range(N):
    for j in range(i+1, N):
        if seats[i] != '1' or seats[j] != '1':
            continue
        if max_cnt < j - i:
            max_cnt = j - i
            max_i, max_j = i, j
        break

mid = (max_i + max_j) // 2
min_cnt = min(mid - max_i, max_j - mid)


if seats[0] == '0':
    for i in range(N):
        if seats[i] == '1':
            min_cnt = max(min_cnt, i - 0)
            break
if seats[N-1] == '0':
    for i in range(N-1, -1, -1):
        if seats[i] == '1':
            min_cnt = max(min_cnt, N - 1 - i)
            break
print(min_cnt)

