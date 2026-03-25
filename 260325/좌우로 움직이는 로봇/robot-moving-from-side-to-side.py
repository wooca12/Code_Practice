n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

def time_position(t, d):
    array = [0]
    for s, l in zip(t, d):
        for i in range( s):
            if l == 'R':
                array.append(array[-1] + 1)
            else:
                array.append(array[-1] - 1)
    return array

a_position = time_position(t, d)
b_position = time_position(t_b, d_b)

count = 0

a_id, b_id = 0, 0
for i in range(1, max(len(a_position), len(b_position))):
    a_id = i if i < len(a_position) else a_id
    b_id = i if i < len(b_position) else b_id
    if a_position[a_id] == b_position[b_id] and a_position[a_id-1] != b_position[b_id-1]:
        count += 1
print(count)