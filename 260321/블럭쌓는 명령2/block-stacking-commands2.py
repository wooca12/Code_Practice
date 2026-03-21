N, K = map(int, input().split())

commands = [list(map(int, input().split())) for _ in range(K)]
array = [0] * N

for c in commands:
    for i in range(c[0] - 1 , c[1]):
        array[i] = array[i] + 1

print(max(array))