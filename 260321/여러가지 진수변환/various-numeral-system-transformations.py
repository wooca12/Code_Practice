N, B = map(int, input().split())

# Please write your code here.

array = []
while True:
    if N < B:
        array.append(N)
        break

    array.append(N % B)
    N = N // B

print(array)
for i in array[::-1]:
    print(i, end=' ')