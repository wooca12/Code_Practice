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
eat_cheese = [set() for _ in range(N + 1)]
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

    eat_cheese[person].add(milk)


sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

def late_sick_time(person, time):
    for i in range(S):
        if person == sick_p[i] and time >= sick_t[i]:
            return True
    return False

def sick_but_not_eat_bad(person, bad_cheese):
    if person in sick_p and bad_cheese not in eat_cheese[person]:
        return True
    return False

def eat_bad_but_not_sick(person, bad_cheese):
    if bad_cheese in eat_cheese[person] and person not in sick_p:
        return True
    return False
    
max_count = 0

for bad_cheese in range(1, M + 1):
    need_person = set()
    for person, cheese, time in zip(p, m, t):
        # 지금 먹은게 상한 치즈 아니라명
        if cheese != bad_cheese:
            continue
        # 지금 먹은게 상한 치즈라면
        # 1. 무조건 아파야 함, 2. 먹은 시간 < 아픈 시간 
        # if 이미 받았는데 또 먹었을 경우 -> 시간 관계 없음
        if person not in sick_p:
            need_person.add(person)
        for i in range(S):
            if person == sick_p[i] and time < sick_t[i]:
                need_person.add(person)
        
            

        
        # 모순 1. sick & not eat bad
        # 모순 2. sick & eat bad & late sick time
        # 모순 3. eat bad & not sick
      
    max_count = max(max_count, len(need_person))
            


print(max_count)
            
