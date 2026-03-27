board = [list(map(int, input().split())) for _ in range(19)]

def print_5x5(grid):
    print()
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end=' ')
        print()
    print()

def check_5x5_grid(grid):
    winner, x, y = 0, 0, 0
    # 가로, 세로
    for r in range(5):
        sum_r, sum_c = 0, 0
        for c in range(5):
            sum_r += grid[r][c]
            sum_c += grid[c][r]
        if sum_r == 5 or sum_r == 10:
            winner, x, y = sum_r // 5, r, c - 2
        elif sum_c == 5 or sum_c == 10:
            winner, x, y = sum_c // 5, r - 2, c
    # 대각선 \ /
    # 00 11 22 33 44 / 40 31 22 23 13 04
    sum_a, sum_b = 0, 0
    for r in range(5):
        sum_a += grid[r][r]
        sum_b += grid[r][4-r]

    if sum_a == 5 or sum_b == 5:
        winner, x, y = 1, 2, 2
    elif sum_a == 10 or sum_b == 10:
        winner, x, y = 2, 2, 2

    return winner, x, y



flag = False
winner, x, y = 0, 0, 0

for i in range(15):
    for j in range(15):
        winner, a, b = check_5x5_grid([board[i][j:j+5] for i in range(i, i+5)])
        if winner != 0 :
            flag = True
            x, y = i + a + 1, j + b + 1
            break
    if flag:
        break
print(winner)
if flag:
    print(x, y)




