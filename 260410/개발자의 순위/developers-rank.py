k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]
new_arr = []

for i in range(k):
    r = [0] * n
    for j in range(n):
        rank = j + 1
        dev_num = arr[i][j] - 1
        r[dev_num] = rank

    new_arr.append(r)
    

    
count = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        flag = True

        for l in range(k):
            contest = new_arr[l]
            if contest[i] >= contest[j]:
                flag = False
                break
            
        if flag :
            count += 1
print(count)
