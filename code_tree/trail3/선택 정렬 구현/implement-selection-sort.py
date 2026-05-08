n = int(input())
arr = list(map(int, input().split()))


for i in range(n):
    min = i
    for j in range(i + 1, n):
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
    


for i in arr:
    print(i, end=' ')