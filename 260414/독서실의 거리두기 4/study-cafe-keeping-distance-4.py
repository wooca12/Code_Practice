N = int(input())
seat = input()
s_indices = [i for i in range(N) if seat[i] == '1']

maxmin = 0 

def min_dist(i1, i2):
    tmp = [n for n in s_indices]
    tmp.append(i1)
    tmp.append(i2)
    tmp.sort()
    min_d = N
    for i in range(1, len(tmp)):
        dist = tmp[i] - tmp[i-1]
        min_d = min(min_d, dist)
    return min_d

for i in range(N):
    for j in range(i+1, N):
        if seat[i] == '1' or seat[j] == '1':
            continue
        maxmin = max(maxmin, min_dist(i, j))
        
print(maxmin)
