n = int(input())
segments = [tuple(input().split()) for _ in range(n)]

offset = 100
blocks = [0] * 200


cur = 0
cur += offset
for x, d in segments:
    for i in range(int(x)):
        if d == 'R':
            blocks[cur] += 1
            cur = cur + 1
        elif d == 'L':
            cur = cur - 1
            blocks[cur] += 1

count = 0
for i in range(len(blocks)):
    if blocks[i] >= 2:
        count += 1
print(count)



