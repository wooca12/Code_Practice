class EatRecord:
    def __init__(self, p, m, t):
        self.p, self.m, self.t = p, m, t

class SickRecord:
    def __init__(self, p, t):
        self.p, self.t = p,t 

N, M, D, S = tuple(map(int, input().split()))
eat = []
for _ in range(D):
    p, x, t = tuple(map(int, input().split()))
    eat.append(EatRecord(p, x, t))

sick = []
for _ in range(S):
    p, t = tuple(map(int, input().split()))
    sick.append(SickRecord(p, t))


max_pills = 0
for bad_m in range(1, M + 1):

    # 상한 치즈 먹은 시간 저장
    time = [0] * (N+1)
    for info in eat:
        if info.m != bad_m:
            continue
        if time[info.p] == 0 or info.t < time[info.p]:
            time[info.p] = info.t

    # 상한 치즈 안먹었거나 시간 모순 시 
    possible = True
    for info in sick:
        if time[info.p] == 0:
            possible = False
        elif time[info.p] >= info.t:
            possible = False
    
    # 약 개수
    pills = 0
    if possible:
        for i in range(1, N+1):
            if time[i] != 0:
                pills += 1
    
    max_pills = max(max_pills, pills)

print(max_pills)
