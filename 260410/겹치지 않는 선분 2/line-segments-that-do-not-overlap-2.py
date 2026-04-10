n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        a1, a2 = lines[i]
        b1, b2 = lines[j]
        if (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2):
            count += 1
print(len(lines) - count)