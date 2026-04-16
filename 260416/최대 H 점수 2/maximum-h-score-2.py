import sys
N, L = map(int, input().split())
a = list(map(int, input().split()))

max_h = 0

change = [False] * N

def count_possible(arr, h):
    count = 0
    for i in range(N):
        if arr[i] >= h:
            count += 1
    return count


for h in range(N+1, 1, -1):
    # h : h 이상의 수 h개 이상 만족한 최댓값

    # 적어도 만족해야하는 숫자 개수
    origin_cnt = count_possible(a, h)
    change_cnt = 0
    

    for i in range(N):
        if a[i] == True:
            continue
        # 변화 <= L개 & H 조건 만족할 때 
        # 변화 < L개도 포함하는 이유: h 보다 높은 숫자 아무거나 L개 +1하면 되기 때문에 변화 상관 없음
        if change_cnt <= L and count_possible(a, h) >= h:
            print(h)
            sys.exit()
        elif change_cnt < L and count_possible(a, h) < h:
            a[i] += 1
            change[i] = True
            change_cnt += 1
            # 변화를 주어도 개수 변화가 없으면 원상 복귀
            if count_possible(a,h) == origin_cnt:
                a[i] -= 1
                change[i] = False
                change_cnt -= 1



    

