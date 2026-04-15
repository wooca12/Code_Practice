N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

max_size = 0
max_n = 0
set_num = set(num)

for i in set_num:
    indices = []
    # 같은 번호를 갔는 모든 인덱스
    for j in range(N):
        if i == num[j]:
            indices.append(j)
    size = len(indices)

    # 인접한 거리가 K 이내 일때 터지는 횟수
    for j in range(size - 1):
        dist = indices[j+1] - indices[j]
        if dist > K:
            size -= 1
    # 터진 횟수가 최대라면 번호와 횟수 갱신
    if size > 1 and size > max_size:
        max_n = i
        max_size = size
    
print(max_n)