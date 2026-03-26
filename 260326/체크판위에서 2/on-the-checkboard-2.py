R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]
MAX = 2
count = 0
init_x, init_y = 0, 0
final_x, final_y = R-1, C-1


for i in range(init_x + 1, R):
    for j in range(init_y + 1, C):
        if grid[i][j] != grid[init_x][init_y]:
            for k in range(i + 1, final_x):
                for l in range(j + 1, final_y):
                    if grid[k][l] != grid[i][j] and grid[k][l] != grid[final_x][final_y]:
                        count += 1


print(count)