A = input()
l = len(A)
count = 0
for i in range(l - 1):
    for j in range(i + 1, l):
        if A[i] == '(' and A[j] == ')':
            count += 1
print(count)