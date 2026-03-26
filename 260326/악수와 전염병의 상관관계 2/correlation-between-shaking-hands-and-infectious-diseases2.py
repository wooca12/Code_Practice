# N : 개발자 수
# T : 번에 걸쳐 t초에 악수 ( 1~250)
# K : 번의 악수만 전염 ( 1~250)
# P : 처음 전염병 걸린 개발자 번호 (1~N)
# t : 악수 시간 ( 1~250)
# x : 악수한 개발자 번호
# y : 악수한 개발자 번호

# return : 각 개발자 음성 여부(0, 1)
N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

count_handshakes = [0] * (N + 1)
answer =  [0] * (N + 1)
answer[P] = 1

time_check = [[0, 0] for _ in range(251)]
for t, x, y in handshakes:
    time_check[t][0] = x
    time_check[t][1] = y

for x, y in time_check:
    if x + y == 0:
        continue
    # x와 y 중 한명이라도 감염 & K번 악수 동안만 전파
    # 전염된 x-y끼리도 전파 횟수 포함, 재감염은 아님
    if answer[x] == 1 and count_handshakes[x] < K:
        count_handshakes[x] += 1
        if answer[y] == 0:
            answer[y] = 1
        else:
            count_handshakes[y] += 1
    elif answer[y] == 1 and count_handshakes[y] < K:
        count_handshakes[y] += 1
        if answer[x] == 0:
            answer[x] = 1
        else:
            count_handshakes[x] += 1


for i in answer[1:]:
    print(i, end='')
