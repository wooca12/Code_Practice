X, Y = map(int, input().split())

count = 0
for num in range(X, Y+1):
    arr = [int(i) for i in str(num)]

    n = len(arr) 

    pallindrom = True
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            pallindrom = False
            break
    if pallindrom:
        count += 1

print(count)