import sys
N, L = map(int, input().split())
a = list(map(int, input().split()))

max_h = 0

for h in range(1, N+1):
    # 원소 개수가 n이면 h의 이상의 최대 개수는 n이

    # h-1인 값은 최대 L까지 올릴 수 있음
    # cnt : h 이상인 수 개수 (i-1의 수는 L까지 카운트)
    # cntl : 1 증가시킨 숫자 개수
    cnt = 0
    cntl = 0 

    for j in range(N):
        if a[j] >= h :
            cnt += 1
        elif a[j] == h - 1:
            if cntl < L:
                cntl += 1
                cnt += 1
    if cnt >= h:
        max_h = h
print(max_h)
