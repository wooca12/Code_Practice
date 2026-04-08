n = int(input())
arr = list(map(int, input().split()))

total = 0

for i in range(n):
    for j in range(i, n):
        if len(arr[i:j+1]) == 1:
            total += 1
        elif sum(arr[i:j+1]) / len(arr[i:j+1]) in arr[i:j+1]:
            total +=1
print(total)