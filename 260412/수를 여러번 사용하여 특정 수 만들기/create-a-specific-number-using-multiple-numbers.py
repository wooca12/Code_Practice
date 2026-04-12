A, B, C = map(int, input().split())

max_sum = 0
for a in range(1001):
    sum_a = A * a
    for b in range(1001):
        sum_b = B * b
        if sum_a + sum_b > C:
            break
        else:
            max_sum = max(max_sum, sum_a + sum_b)
print(max_sum)
        

        
    
