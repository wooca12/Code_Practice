inp = [[int(n) for n in input()] for _ in range(3)]

def win(p1, p2):
    # 가로 
    for i in range(3):
        c1, c2 = 0, 0
        for j in range(3):
            if p1 == inp[i][j]:
                c1 += 1
            elif p2 == inp[i][j]:
                c2 += 1

        if c1 + c2 == 3 and c1 > 0 and c2 > 0:
            return True

    # 세로
    for i in range(3):
        c1, c2 = 0, 0
        for j in range(3):
            if p1 == inp[j][i]:
                c1 += 1
            elif p2 == inp[j][i]:
                c2 += 1
        if c1 + c2 == 3 and c1 > 0 and c2 > 0:
            return True

    # 대각선 1
    c1, c2 = 0, 0
    for i in range(3):
        if p1 == inp[i][i]:
                c1 += 1
        elif p2 == inp[i][i]:
            c2 += 1
    if c1 + c2 == 3 and c1 > 0 and c2 > 0:
        return True

    # 대각선 2
    c1, c2 = 0, 0
    for i in range(3):
        if p1 == inp[2-i][i]:
                c1 += 1
        elif p2 == inp[2-i][i]:
            c2 += 1

    if c1 + c2 == 3 and c1 > 0 and c2 > 0:
        return True

    return False
    
    
# inp2 = [[inp[i][j] for i in range(3)] for j in range(3)]
# inp3 = [inp[i][i] for i in range(3)]
# inp4 = [inp[2-i][i] for i in range(3)]

# def win(p1, p2):
#     # 가로 / 세로
#     flag = True
#     a = set([p1, p2])
#     for i in range(3):
#         if len(a ^ set(inp[i])) == 0:
#             return True
#         elif len(a ^ set(inp2[i])) == 0:
#             return True
#     if len(a ^ set(inp3)) == 0:
#             return True
#     elif len(a ^ set(inp4)) == 0:
#         return True
#     return False
        
            
        
count = 0
for i in range(1, 10):
    for j in range(i+1, 10):
        if win(i, j):
            count += 1
print(count)
