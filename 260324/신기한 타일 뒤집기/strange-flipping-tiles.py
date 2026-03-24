# 일렬 회색
# x L ; 왼쪽 이동, x번 뒤집음 흰색
# x R : 오른쪽 이동, x번 뒤집음 검은색
# (현재 타일 포함)
# 실행 후 흰, 검 타일 수

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

OFFSET = 100000
blocks = [0] * (2 * OFFSET + 1)
cur_idx = 0
count_b, count_w = 0, 0

for num, direction in commands:
    num = int(num)
    if direction == 'R':
        for i in range(cur_idx, cur_idx + num, 1):
            if blocks[i] != 1:
                count_b += 1
            if blocks[i] == 2:
                count_w -= 1
            blocks[i] = 1 # black
            cur_idx = i
    elif direction == 'L':
        for i in range(cur_idx, cur_idx - num, -1):
            if blocks[i] != 2:
                count_w += 1
            if blocks[i] == 1:
                count_b -= 1
            blocks[i] = 2  # white
            cur_idx = i

print(count_w, count_b)


