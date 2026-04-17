import sys
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

ans = 'No'
for i in range(n):
    # i번째 제거
    min_x2 = 100
    max_x1 = 0
    for j in range(n):
        if i == j:
            continue
        max_x1 = max(max_x1, x1[j])
        min_x2 = min(min_x2, x2[j])

    if max_x1 <= min_x2:
        ans = 'Yes'
        break
print(ans)
        
