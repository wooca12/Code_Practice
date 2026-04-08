N = int(input())
a, b, c = map(int, input().split())

total = N * N * N
count = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if abs(i - a) > 2 and abs(j - b) > 2 and abs(k - c) > 2:
                count += 1
print(total - count)