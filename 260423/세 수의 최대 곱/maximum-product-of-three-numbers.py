import sys
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

INIT_NUM = sys.maxsize
maxnum = - INIT_NUM
minus, plus = [], []

for i in range(n):
    if arr[i] < 0:
        minus.append(arr[i])
    elif arr[i] > 0:
        plus.append(arr[i])

# Case 1: 양수 x 양수 x 양수 -> 제일 큰 양수값
if len(plus) >= 3:
    maxnum = max(maxnum, plus[-1] * plus[-2] * plus[-3])
# Case 2: 음수 x 음수 x 양수 -> 제일 작은 음수값, 제일 큰 양수 값
if len(minus) >= 2 and len(plus) >= 1:
    maxnum = max(maxnum, minus[0] * minus[1] * plus[-1])
 # Case 3: 양수 x 양수 x 음수 x  -> 절댓값 모두 작은거
if len(minus) >= 1 and len(plus) >= 2:
    maxnum = max(maxnum, minus[-1] * plus[0] * plus[1])
# Case 4: 음수 x 음수 x 음수 -> 모두 작은거
if len(minus) >= 3:
    maxnum = max(maxnum, minus[-1] * minus[-2] * minus[-3])
# Case 3: 0 
if 0 in arr:
    maxnum = max(maxnum, 0)
    
print(maxnum)