n = int(input())
arr = list(input().split())

### answer
arr = [0] + arr
ans = 0
for i in range(1, n+1):
    # A, B, C, D ...
    c = chr(ord('A') + i - 1)

    # 알파벳 인덱스 찾기
    idx = 0
    for j in range(1, n+1):
        if arr[j] == c:
            idx = j
    # 알파벳을 원래 인덱스로 옮기기
    for j in range(idx, i, -1):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        ans += 1
print(ans)

### bubble sort
# cnt = 0
# for i in range(n):
#     for j in range(0, n - 1 - i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             cnt += 1
# print(cnt)