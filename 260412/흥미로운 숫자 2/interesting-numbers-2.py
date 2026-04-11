X, Y = map(int, input().split())


            
count = 0
for num in range(X, Y + 1):
    n_arr = [int(n) for n in str(num)]
    
    freq_num  = [0] * 10
    for n in n_arr:
        freq_num[n] += 1

    flag1 = False    
    flag2 = False
    for i in range(10):
        if not flag1 and freq_num[i] == 1:
            flag1 = True
        if not flag2 and freq_num[i] >= 2:
            flag2 = True
    if flag1 and flag2:
        count += 1
       
        


print(count)
