N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

max_len = 0
for i in range(N):
    tmp = [arr[i]]
    for j in range(i+1, N):
        tmp.append(arr[j])
        if max(tmp) - min(tmp) > K:
            tmp.pop()
    max_len = max(max_len, len(tmp))
print(max_len)
