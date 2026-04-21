a = list(map(int, input().split()))
maxmove = 0

# 움직일 필요 없음
if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
    maxmove = 0

# 오른쪽 끝 사람이 가장 먼저 이동: 최대 횟수 (0번~1번 거리 - 1)회
maxmove = max(maxmove, a[1] - a[0] - 1)
# 왼쪽 끝 사람이 가장 먼저 이동: 최대 횟수 (1~2번 거리 - 1)회
maxmove = max(maxmove, a[2] - a[1] - 1)
print(maxmove)