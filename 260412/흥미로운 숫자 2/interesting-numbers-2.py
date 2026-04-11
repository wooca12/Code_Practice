X, Y = map(int, input().split())


count = 0

for num in range(X, Y+1):
    n_arr = [int(i) for i in str(num)]

    freq_num = [0] * 10
    all_num = 0

    for n in n_arr:
        freq_num[n] += 1
        all_num += 1
    
    interest = False
    for i in range(10):
        if freq_num[i] == all_num - 1:
            interest = True
    if interest:
        count += 1
        
# count = 0
# for num in range(X, Y + 1):
#     n_arr = [int(n) for n in str(num)]
    
#     freq_num  = [0] * 10
#     two_num = []
#     for n in n_arr:
#         freq_num[n] += 1
#         if n not in two_num:
#             two_num.append(n)

#     if len(two_num) != 2:
#         continue
#     if freq_num[two_num[0]] ==1 and freq_num[two_num[1]] >= 2:
#         count += 1
#     elif freq_num[two_num[0]] >= 2 and freq_num[two_num[1]] == 1:
#         count += 1
    
        
print(count)
