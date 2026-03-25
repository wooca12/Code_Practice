OFFSET = 10000
MAX = 2 * OFFSET

n, m = map(int, input().split())

a_commend = []
b_commend = []
for _ in range(n):
    a_commend.append(tuple(input().split()))
for _ in range(m):
    b_commend.append(tuple(input().split()))

def simulator(n, commands):
    array = [0] * (MAX + 1)
    cur_p = 0
    cur_s = 0
    for dir, sec in commands:
        sec = int(sec)
        for _ in range(1, sec+1):
            if dir == 'R':
                cur_p += 1
                cur_s += 1
                array[cur_s] = cur_p
            else:
                cur_p -=1
                cur_s += 1
                array[cur_s] = cur_p
    return array


a_array = simulator(n, a_commend)
b_array = simulator(m, b_commend)


for i in range(MAX + 1):
    if i !=0 and a_array[i] == b_array[i]:
        print(i)
        break