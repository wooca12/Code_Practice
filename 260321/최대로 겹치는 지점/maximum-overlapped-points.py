n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
array =[0] * 100
for s in segments:
    for i in range(s[0], s[1]+1):
        array[i] = array[i] + 1

print(max(array))
