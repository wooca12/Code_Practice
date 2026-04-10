n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

count = [1] * n
for i in range(n):
    for j in range(i+1, n):
        if i == j :
            continue
        a1, a2 = lines[i]
        b1, b2 = lines[j]
        if (a1 - b1) * (a2 - b2) <= 0:
            count[i] = 0
            count[j] = 0
print(sum(count))