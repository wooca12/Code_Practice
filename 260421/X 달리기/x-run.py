import sys
X = int(input())
time = 0
left_dist = X
v = 1

while True:
    left_dist -= v
    time += 1

    # 목적지 도달 시 멈춤
    if left_dist == 0:
        break

    # 속도를 높여도 괜찮을 때
    if left_dist >= (v + 1) * (v * 2) / 2:
        v += 1
    # 속도를 유지해도 괜찮을 때
    elif left_dist >= v * (v + 1) / 2:
        pass
    # 둘 다 만족 못하면 속도 줄임
    else:
        v -= 1
        
print(time)


# min_time = 10000
# for point in range(X):
#     dist = 0
#     speed = 0
#     for t in range(10000):
#         dist += speed

#         if speed < 0:
#             break
#         if dist == X and speed == 1:
#             min_time = min(min_time, t)
#             break
#         if dist < point:
#             speed += 1
#         elif dist >= point:
#             remain = X - dist
#             need = (speed + 1) * speed // 2
#             if remain < need:
#                 speed -= 1

        


# print(min_time)