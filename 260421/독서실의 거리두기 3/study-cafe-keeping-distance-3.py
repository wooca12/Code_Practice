N = int(input())
seats = [int(i) for i in input()]
maxmin = 0

for i in range(N):
    if seats[i] == 1:
        continue

    seats[i] = 1
    pos = [i for i in range(N) if seats[i] == 1]

    min_diff = 10000
    for j in range(1, len(pos)):
        min_diff = min(min_diff, abs(pos[j] - pos[j-1]))

    maxmin = max(maxmin, min_diff)

    seats[i] = 0


print(maxmin)