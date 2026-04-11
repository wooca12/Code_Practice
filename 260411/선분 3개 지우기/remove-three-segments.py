n = int(input())
lines = []
for _ in range(n):
    left, right = map(int, input().split())
    lines.append((left, right))

count = 0

def is_overlap(i, j, k):
    arr = [0] * 101
    for l in range(n):
        if l in [i, j, k]:
            continue
        left, right = lines[l]
        for p in range(left, right + 1):
            arr[p] += 1
            if arr[p] > 1 : 
                return True
    return False


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            stop = False
            # i, j, k 선분 제외한 나머지 선분 겹치는지 검사
            if not is_overlap(i, j, k):
               count += 1
print(count)