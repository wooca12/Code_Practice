import sys
INIT_MIN = sys.maxsize
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

min_length = INIT_MIN

for i in range(n):
    min_a, max_b = INIT_MIN, -INIT_MIN
    for j in range(n):
        if i == j:
            continue
        min_a = min(min_a, segments[j][0])
        max_b = max(max_b, segments[j][1])
    min_length = min(min_length, max_b - min_a)

print(min_length)
        
    
