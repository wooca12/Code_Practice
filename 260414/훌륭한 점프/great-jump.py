n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX = 100

def is_possible(max_val):
    last_id = 0 # 시작번호

    for i in range(1, n):
        if arr[i] <= max_val: # 돌의 번호가 max_val보다 작음
            if i - last_id > k: # 거리가 k보다 크면 아웃
                return False
            last_id = i # 다음 돌
    return True

for i in range(max(arr[0], arr[n-1]), MAX + 1):
    # i : 지나간 번호의 최대값일때
    if is_possible(i):
        print(i)
        break


# def is_possible(max_val):
#     available_indices = []
#     # 시작돌 추가
#     available_indices.append(0)

#     # max_val 이하인 돌 모두 추가
#     for i, elem in enumerate(arr):
#         if elem <= max_val:
#             available_indices.append(i)

#     # 마지막 돌 추가
#     available_indices.append(n-1)

#     arr_size = len(available_indices)
#     for i in range(1, arr_size):
#         dist = available_indices[i] - available_indices[i-1]
#         # 돌 간의 거리가 k 아싱이면 안됨
#         if dist > k:
#             return False

#     return True


# minmax = 100

# for a in arr[1:n-1]:
#     # 최대값이 a 일때 조건을 만족하는지 검사
#     if is_possible(a):
#         # a들 중에서도 최소인 경우
#         minmax = min(minmax, max(a, arr[0], arr[-1]))
# print(minmax)