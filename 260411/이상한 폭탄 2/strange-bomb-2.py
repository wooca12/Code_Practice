N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# 폭탄 개수 N
# 특정 거리 K
# 같은 번호 부여된 폭탄끼리 거리가 K 안에 있으면
# return : 폭발 폭탄 중 가장 큰 번호

max_num = -1

for i in range(N):
    bum = False
    for j in range(i+1, N):
        if num[i] == num[j] and (j - i) <= K:
            bum = True
        if bum:
            max_num = max(max_num, num[i])


print(max_num)
