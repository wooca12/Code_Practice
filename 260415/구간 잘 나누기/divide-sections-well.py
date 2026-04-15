import sys
n, m = map(int, input().split())
a = list(map(int, input().split()))


minmax = sys.maxsize
MAX = 10000
for sum in range(1, MAX + 1):
    # 구간의 합의 최대가 sum일 때

    possible = True
    section = 1

    count = 0
    for j in range(n):
        # 해당 숫자가 구간의 합의 최대값보다 크면 안됨
        if a[j] > sum:
            possible = False
            break
        # 구간에 해당 숫자가 더 해졌을때 최대값보다 큼 -> 해당 숫자를 다음 구간으로 만듦
        if count + a[j] > sum:
            count = 0
            section += 1
        # 구간에 해당 숫자를 집어 넣는다
        count += a[j]

    if possible and section <= m:
        minmax = min(minmax, sum)
print(minmax)

