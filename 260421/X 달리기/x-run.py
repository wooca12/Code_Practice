import sys
X = int(input())

min_time = 10000
for point in range(X):
    dist = 0
    speed = 0
    for t in range(10000):
        dist += speed
        if speed < 0:
            break
        if dist == X and speed == 1:
            min_time = min(min_time, t)
            break
        if dist < point:
            speed += 1
        elif dist >= point:
            remain = X - dist
            need = (speed + 1) * speed // 2
            if remain < need:
                speed -= 1

        


print(min_time)