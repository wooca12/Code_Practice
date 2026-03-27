import sys
n = int(input())
a = [int(input()) for _ in range(n)]

min_dist = sys.maxsize
for i in range(n): # i 시작 방
    dist = 0
    # print(i)
    for j in range(n):
        d = j - i if j>=i else j - i + n # 사람마다 가야할 거리
        # print('{}번째 방, 사람수 {}, 거리{}, {}'.format(j, a[j], d, a[j] * d))
        dist += a[j] * d
    # print('최종거리', dist)
    min_dist = min(min_dist, dist)

print(min_dist)