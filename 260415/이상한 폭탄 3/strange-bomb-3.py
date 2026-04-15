N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

MAX = 1000000
maxval = 1
maxidx = 0

bomb = [0] * (MAX + 1) # 번호마다 터진 횟수 카운트
exploded = [False] * N # 주어진 폭탄이 터졌는지 체크

for i in range(N):
    for j in range(i+1, N):
        # 거리가 K 초과면 넘어감
        if j - i > K:
            break
        # 번호가 같지 않으면 안터짐
        if num[i] != num[j]:
            continue
         
        # 인접한 i, j 번호 폭탄이 터졌는지 여부와 횟수를 갱신
        # 번호가 같으면 터짐
        # 이미 터졌는지 확인 -> 안터지면 갱신
        if exploded[i] == False:
            bomb[num[i]] += 1
            exploded[i] = True

        if exploded[j] == False:
            bomb[num[j]] += 1
            exploded[j] = True


for i in range(MAX + 1):
    if maxval <= bomb[i]:
        maxval = bomb[i]
        maxidx = i
print(maxidx)
            
        



# max_size = 0
# max_n = 0
# set_num = set(num)

# for i in set_num:
#     indices = []
#     # 같은 번호를 갔는 모든 인덱스
#     for j in range(N):
#         if i == num[j]:
#             indices.append(j)
#     size = len(indices)

#     # 인접한 거리가 K 이내 일때 터지는 횟수
#     for j in range(size - 1):
#         dist = indices[j+1] - indices[j]
#         if dist > K:
#             size -= 1
#     # 터진 횟수가 최대라면 번호와 횟수 갱신
#     if size > 1 and size > max_size:
#         max_n = i
#         max_size = size
    
# print(max_n)