N = int(input())
seats = [int(i) for i in input()]

# 사용중인 좌석 번호 구함
def get_pos(seats):
    pos_indices = []
    for i in range(N):
        if seats[i] == 1:
            pos_indices.append(i)
    return pos_indices

# 좌석 간 가장 거리가 넓은 좌석 1쌍
max_i, max_j= 0, 0
max_diff = 0
pos = get_pos(seats)
for i in range(1, len(pos)):
    if pos[i] - pos[i-1] > max_diff :
        max_diff = pos[i] - pos[i-1]
        max_i, max_j = pos[i-1], pos[i]

# 넓은 좌석 중간에 1 놓음
seats[(max_i + max_j) //2 ] = 1
new_pos = get_pos(seats)

# 좌석 간 가장 거리가 가까운 좌석 1쌍
ans = 1000
for i in range(1, len(new_pos)):
    ans = min(ans, new_pos[i] - new_pos[i-1]) 

print(ans)

####################################################

# maxmin = 0
# for i in range(N):
#     if seats[i] == 1:
#         continue

#     seats[i] = 1
#     pos = [i for i in range(N) if seats[i] == 1]

#     min_diff = 10000
#     for j in range(1, len(pos)):
#         min_diff = min(min_diff, abs(pos[j] - pos[j-1]))

#     maxmin = max(maxmin, min_diff)

#     seats[i] = 0


# print(maxmin)