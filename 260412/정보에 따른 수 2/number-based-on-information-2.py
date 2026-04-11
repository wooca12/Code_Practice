T, a, b = map(int, input().split())

info = []
for _ in range(T):
    char, pos = input().split()
    info.append((char, int(pos)))

count = 0
for x in range(a, b + 1):
    min_d1, min_d2 = 1000, 1000
    for i in range(T):
        char, pos = info[i]
        if char == 'S':
            min_d1 = min(min_d1, abs(x - pos))
        elif char == 'N':
            min_d2 = min(min_d2, abs(x - pos))
    if min_d1 <= min_d2:
        count += 1

print(count)
