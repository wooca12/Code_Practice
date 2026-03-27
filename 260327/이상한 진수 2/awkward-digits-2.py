
a = input()
a = [int(i) for i in a]
length = len(a)
max_num = 0
num = 0

# i번째 바뀐 후 나머지 이진 수 계산
def change_arr(i, n, arr):
    new = 0 if arr[i]== 1 else 1
    n = n * 2 + new

    for x in range(i + 1, length):
        n = n * 2 + arr[x]
    return n

num = num * 2 + a[0]
for i in range(1, length):
    for j in range(i, length):
        new_num = change_arr(i, num, a)
        max_num = max(max_num, new_num)
    num = num * 2 + a[i]

print(max_num)