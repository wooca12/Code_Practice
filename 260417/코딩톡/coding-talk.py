import sys
n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# n명, m개 메시지, p번째 문자
if u[p-1] == 0:
    sys.exit()

for i in range(n):
    person = chr(ord('A') + i)
    read = False

    for j in range(m):
        # message 보낸사람이 맞음 + p 메시지 읽은 수와 크거나 같음 
        if c[j] == person and u[j] >= u[p-1]:
            read = True

    if read == False:
        print(person, end = ' ')

    
        