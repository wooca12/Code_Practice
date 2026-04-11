X, Y = map(int, input().split())

max_sum = 0

for num in range(X, Y+1):
    sum_n = 0
    n = num
    while True:
        if n < 10:
            sum_n += n
            break
        sum_n += n % 10
        n = n // 10
    max_sum = max(max_sum, sum_n)    
print(max_sum)
    
    