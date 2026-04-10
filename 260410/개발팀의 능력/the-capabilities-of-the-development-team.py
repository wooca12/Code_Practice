arr = list(map(int, input().split()))
n = len(arr)
min_diff = 100
flag = False

def get_sum(i, j, k):
    sum1 = arr[i] + arr[j]
    sum2 = arr[k]
    sum3 = sum(arr) - sum1 - sum2

    return sum1, sum2, sum3

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                a, b, c = get_sum(i, j, k)
                if a != b != c:
                    min_diff = min(min_diff, abs(max(a,b,c) - min(a,b,c)))
                    flag = True
if flag: 
    print(min_diff)
else:
    print(-1)