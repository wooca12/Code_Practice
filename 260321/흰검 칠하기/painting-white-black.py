n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# L : 왼쪽, 현재 포함 x칸 흰색
# R : 오른쪽, 현재 포함 x 검은칸

# 흰 검 회
# 1
offset = 10
blocks = [0] * 20
cur = 0
cur += offset
for i in range(n):
    for _ in range(x[i]):
        if dir[i] == 'L':
            cur -= 1
            blocks[cur] = blocks[cur] * 10 + 1
        elif dir[i] == 'R':
            blocks[cur] = blocks[cur] * 10 + 2
            cur += 1


def is_gray(num):
    black_count = 0
    white_count = 0
    while True:
        if num < 10:
            if num % 10 == 1:
                white_count += 1
            elif num % 10 == 2:
                black_count += 1
            break
        if num % 10 == 1:
            white_count += 1
        elif num % 10 == 2:
            black_count += 1
        num //= 10

    if white_count >= 2 and black_count >= 2:
        return True

    return False

count = [0, 0, 0]

for i in range(len(blocks)):
    if blocks[i] >= 1000 and is_gray(blocks[i]):
        count[2] += 1 # 회색
    else:
        blocks[i] = blocks[i] % 10
        if blocks[i] == 2:
            count[1] += 1 # 검은색
        elif blocks[i] == 1:
            count[0] += 1

for i in count:
    print(i, end=' ')


