n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

max_score = 0
for i in range(3):
    score = 0
    arr = [0] * 3
    arr[i] = 1
    for a, b, c in moves:
        arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
        if arr[c-1] == 1:
            score += 1
    max_score = max(max_score, score)
print(max_score)