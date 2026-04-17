n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(n):
    if A[i] > B[i]:
        num = A[i] - B[i]
        A[i] -= num
        A[i+1] += num
        ans += num
print(ans)