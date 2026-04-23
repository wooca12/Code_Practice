N = int(input())
seats = list(input())

max_cnt = 0
for i in range(N):
    if seats[i] == '1':
        continue
    seats[i] = '1'
    min_cnt = N
    for j in range(N):
        for k in range(j+1, N):
            if seats[j] == '1' and seats[k] == '1':
                min_cnt = min(min_cnt, abs(j-k))
    max_cnt = max(max_cnt, min_cnt)
    seats[i] = '0'
print(max_cnt)