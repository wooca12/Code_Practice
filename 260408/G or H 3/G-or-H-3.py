n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

arr = [0] * 10001

for i in range(n):
    if c[i] == "G":
        arr[x[i]] = 1
    elif c[i] == 'H':
        arr[x[i]] = 2
    else:
        arr[x[i]] = 0


max_score = 0
for i in range(1, 10001 - k):
    score = 0
    for j in range(i, i + k + 1) :
        score += arr[j] 
    max_score = max(max_score, score)

print(max_score)