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

time_check = [[0, 0] for _ in range(250)]
for t, x, y in handshakes:
    time_check[t][0] = x
    time_check[t][1] = y

for x, y in time_check:
    if x == 0 and y == 0:
        continue

    if ((answer[x] == 1 and count_handshakes[x] < 3) or
            (answer[y] == 1 and count_handshakes[y] < 3)) :
        count_handshakes[x] += 1
        count_handshakes[y] += 1
        answer[x], answer[y] = 1, 1

for i in answer:
    print(i, end='')