n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

OFFSET = 100000
blocks = [0] * (2 * OFFSET + 1)
count_b = [0] * (2 * OFFSET + 1)
count_w = [0] * (2 * OFFSET + 1)
cur_index = OFFSET
for num, direction in commands:
    num = int(num)
    if direction == 'L':
        while num > 0:
            blocks[cur_index] = 1
            count_w[cur_index] += 1
            num -= 1
            if num > 0:
                cur_index -= 1
    elif direction == 'R':
        while num > 0:
            blocks[cur_index] = 2
            count_b[cur_index] += 1
            num -= 1
            if num > 0:
                cur_index += 1

w, b, g = 0, 0, 0
for i in range(len(blocks)):
    if count_b[i] == 2 and count_w[i] == 2:
        g += 1
    elif blocks[i] == 1:
        w += 1
    elif blocks[i] == 2:
        b += 1
print(w, b, g)



