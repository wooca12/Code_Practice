n = int(input())
arr = list(map(int, input().split()))

min_sum = 10000

for i in range(n):
    arr[i] *= 2
    for j in range(n):
        remain_arr = [item for k, item in enumerate(arr) if k != j]
        sum = 0
        for k in range(n-2): # 하나 제외한 나머지 숫자
            sum += abs(remain_arr[k] - remain_arr[k+1])
        min_sum = min(min_sum, sum)
    arr[i] //= 2
print(min_sum)