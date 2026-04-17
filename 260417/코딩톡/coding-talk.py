n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# n명, m개 메시지, p번째 문자
all_person = [chr(i) for i in range(ord('A'), ord('A')+ n)]

read = []
for i in range(p-1, n):
    person = c[i]
    if person not in read:
        read.append(person)
num = u[p-1]

for p in all_person:
    if num > 0 and p not in read:
        print(p, end=' ')
    
        