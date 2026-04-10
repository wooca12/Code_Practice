import sys
ability = list(map(int, input().split()))
n = len(ability)
min_diff = sys.maxsize


def get_diff(i, j, k, m):
    sum1 = ability[i] + ability[j]
    sum2 = ability[k] + ability[m]
    sum3 = sum(ability) - sum1 - sum2
    max_sum = max(sum1, sum2, sum3)
    min_sum = min(sum1, sum2, sum3)
    return abs(max_sum - min_sum)

for i in range(n):
    for j in range(n):
        for k in range(n):
            for m in range(n):
                if i != j and i != k and i != m and j != k and j != m and k != m:
                    min_diff = min(min_diff, get_diff(i, j, k, m))
                    
        
            
print(min_diff)
                