# N : 사람 수
# M : 치즈 수 
# D : 치즈 먹은 수
# S : 아픈 기록 수
# D줄 : 사람 p 치즈 m 언제 t
# S줄 : 사람 p 언제 t
# return 최대 약 개수
# 상한 치즈 먹은 후 1초 지나야 아프기 시작

N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

def fail_check_sick(person, time):
    for s in range(S):
        if person == sick_p[s] and time >= sick_t[s]:
            return True
    return False

    
max_count = 0

for i in range(1, M+1):
    bad_cheeze = i
    need_medicine = []
    for j in range(D):
        if m[j] != bad_cheeze:
            continue
        if p[j] not in need_medicine:
            if fail_check_sick(p[j], t[j]):
                break
            else:
                need_medicine.append(p[j])
            
    max_count = max(max_count, len(need_medicine))

print(max_count)
            
