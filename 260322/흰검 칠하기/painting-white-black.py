n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

OFFSET = 100000
blocks = [0] * (2 * OFFSET + 1)
count_b = [0] * (2 * OFFSET + 1)
count_w = [0] * (2 * OFFSET + 1)
cur_index = OFFSET
for num, direction in commands:
    if direction == 'L':
        for i in range(cur_index, cur_index + int(num), 1):
            blocks[i] = 1
            count_w[i] += 1
            cur_index = i
    elif direction == 'R':
        for i in range(cur_index, cur_index - int(num), -1):
            blocks[i] = 2
            count_b[i] += 1
            cur_index = i

w, b, g = 0, 0, 0
for i in range(len(blocks)):
    if count_b[i] == 2 and count_w[i] == 2:
        g += 1
    elif blocks[i] == 1:
        w += 1
    elif blocks[i] == 2:
        b += 1
print(w, b, g)

