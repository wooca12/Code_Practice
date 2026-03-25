# A: 9s front / 3s back  / 5s front
# B; 2s back / 2s front / 12s front
# time: A=B and position A=B
OFFSET = 100000
MAX = 2 * OFFSET

n, m = map(int, input().split())

a_commend = []
b_commend = []
a_times = 0
b_times = 0
for _ in range(n):
    d, t = input().split()
    a_commend.append((d, t))
    a_times += int(t)
for _ in range(m):
    d, t = input().split()
    b_commend.append((d, t))
    b_times += int(t)

def simulator(commands):
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


a_array = simulator(a_commend)
b_array = simulator(b_commend)


ans = -1
for i in range(MAX + 1):
    if i != 0 and a_array[i] == b_array[i]:
        ans = i
        break
    if a_times == 0 or b_times == 0:
        break
    a_times -=1
    b_times -=1
print(ans)
