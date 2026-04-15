N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

max_size = 0
max_n = 0
set_num = set(num)

for i in set_num:
    indices = []
    for j in range(N):
        if i == num[j]:
            indices.append(j)
    size = len(indices)
    for j in range(size - 1):
        dist = indices[j+1] - indices[j]
        if dist > K:
            size -= 1
    if size > 1 and size > max_size:
        max_n = i
        max_size = size
    
print(max_n)