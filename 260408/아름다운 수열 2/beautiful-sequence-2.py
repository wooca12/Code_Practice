N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(N - M + 1):
    exist = True
    for j in range(i, i + M):
        if A[j] not in B:
            exist = False
    if exist: 
        count += 1

print(count)