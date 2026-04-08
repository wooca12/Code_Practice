N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0

for i in range(N - M + 1):
    exist = True
    if sorted(B) == sorted(A[i:i+M]):
        count += 1
print(count)