N = int(input())
seats = list(input())

max_cnt = 0
max_i, max_j = 0, 0
for i in range(N):
    for j in range(i+1, N):
        if seats[j] != '1' or seats[j] != '1':
            continue
        if j - i > max_cnt:
            max_cnt = j - i
            max_i, max_j = i, j
        break
mid = (max_i + max_j) // 2

def get_min(index):
    seats[index] = '1'
    mincnt = N
    for i in range(N):
        for j in range(i+1, N):
            if seats[i] == '1' and seats[j] == '1':
                mincnt = min(mincnt, j - i)
    seats[index] = '0'
    return mincnt

maxmin = get_min(mid)



if seats[0] == '0':
    maxmin = max(maxmin, get_min(0))
if seats[N-1] == '0':
    maxmin = max(maxmin, get_min(N-1))
print(maxmin)