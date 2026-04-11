N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

max_work = 0

def cal_work(t, ta, tb):
    if t < ta:
        return C
    elif ta <= t and t <= tb:
        return G
    elif t > tb:
        return H

for t in range(10001):
    work = 0
    for i in range(N):
        ta, tb = ranges[i]
        work += cal_work(t, ta, tb)
    
    max_work = max(max_work, work)

print(max_work)


            
