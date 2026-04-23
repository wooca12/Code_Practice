board = [list(input()) for _ in range(10)]

lx, ly = 0, 0
rx, ry = 0, 0
bx, by = 0, 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            lx, ly = i, j
        elif board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

if lx != bx and ly != by:
    print(abs(lx - bx) + abs(ly - by) - 1)
elif lx == bx:
    if lx == rx and min(ly, by) <= ry and ry <= max(ly, by):
        print(abs(ly - by) + 1)
    else:
        print(abs(ly - by) - 1)
elif ly == by:
    if ly == ry and min(lx, bx) <= rx and rx <= max(lx, bx) :
        print(abs(lx - bx) + 1)
    else:
        print(abs(lx - bx) - 1)