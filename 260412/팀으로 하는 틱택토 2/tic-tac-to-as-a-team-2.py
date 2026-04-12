inp = [[int(n) for n in input()] for _ in range(3)]

count = 0
inp2 = [[inp[i][j] for i in range(3)] for j in range(3)]
inp3 = [inp[i][i] for i in range(3)]
inp4 = [inp[2-i][i] for i in range(3)]


def win(p1, p2):
    # 가로 / 세로
    flag = True
    a = set([p1, p2])
    for i in range(3):
        if len(a ^ set(inp[i])) == 0:
            return True
        elif len(a ^ set(inp2[i])) == 0:
            return True
    if len(a ^ set(inp3)) == 0:
            return True
    elif len(a ^ set(inp4)) == 0:
        return True
    return False
        
            
        
count = 0
for i in range(1, 10):
    for j in range(i+1, 10):
        if win(i, j):
            count += 1
print(count)
