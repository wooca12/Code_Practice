n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

offset = 100
array =[0] * 200
for s in segments:
    for i in range(s[0]+offset, s[1]+offset):
        array[i] = array[i] + 1

print(max(array))
