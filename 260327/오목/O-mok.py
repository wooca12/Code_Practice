board = [list(map(int, input().split())) for _ in range(19)]

def print_5x5(grid):
    print()
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end=' ')
        print()
    print()

def check_list(arr):
    w = arr[0]
    for i in range(1, len(arr)):
        if w == 0 or arr[i] != w:
            return 0
    return w

def check_5x5_grid(grid):
    # 행검사
    for r in range(5):
        new_list = grid[r]
        winner = check_list(new_list)
        if winner != 0:
            return winner, r, 2
    # 열검사
    for c in range(5):
        new_list = [grid[i][c] for i in range(5)]
        winner = check_list(new_list)
        if winner != 0:
            return winner, 2, c

    # 대각선 \ 검사
    # 00 11 22 33 44 / 40 31 22 23 13 04
    for r in range(5):
        new_list = [grid[i][i] for i in range(5)]
        winner = check_list(new_list)
        if winner != 0:
            return winner, 2, 2
    # 대각선 / 검사
    for c in range(5):
        new_list = [grid[4-i][i] for i in range(5)]
        winner = check_list(new_list)
        if winner != 0:
            return winner, 2, 2

    return 0, 0, 0


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
