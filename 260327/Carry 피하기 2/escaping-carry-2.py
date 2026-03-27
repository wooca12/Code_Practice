n = int(input())
arr = [int(input()) for _ in range(n)]

lenght = len(arr)

max_sum = 0
def is_not_carry(n1, n2, n3):
    result = True
    while n1 != 0 or n2 != 0 or n3 != 0:
        if (n1 % 10) + (n2 % 10) + (n3 % 10) >= 10:
            result = False
            break
        n1, n2, n3 = n1 // 10, n2 // 10, n3 // 10
    return result

flag = 0
for i in range(lenght):
    for j in range(i + 1, lenght):
        for k in range(j + 1, lenght):
            if is_not_carry(arr[i], arr[j], arr[k]):
                flag = 1
                max_sum = max(max_sum, arr[i] + arr[j] + arr[k])

print(max_sum if flag == 1 else -1)
