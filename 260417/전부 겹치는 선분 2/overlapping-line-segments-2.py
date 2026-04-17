import sys
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

for i in range(n):
    # i번째 제거
    min_b = 100
    max_a = 0
    for j in range(n):
        if i == j:
            continue
        if max_a < x1[j]: # 4 7
            max_a = x1[j]
        if min_b > x2[j]: # 4 
            min_b = x2[j]

    if min_b >= max_a:
        print('Yes')
        sys.exit()
print('No')
        
