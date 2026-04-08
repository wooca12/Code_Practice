n = int(input())
people = [tuple(input().split()) for _ in range(n)]

arr = [0] * 101
start = 101
end = 0
for i in range(n):
    pos, chr = int(people[i][0]), people[i][1]
    arr[pos] = chr
    start = min(start, pos)
    end = max(end, pos)
    
max_size = -1

for i in range(start, end + 1):
    for j in range(i, end + 1):
        count_G, count_H = 0, 0
        if arr[i] == 0 or arr[j] == 0:
            continue
        for k in range(i, j+1):
            if arr[k] == 'G':
                count_G += 1
            elif arr[k] == 'H':
                count_H += 1
        

        if 0 not in arr[i:j+1] and (count_G > 0 and count_H == 0 or count_H > 0 and count_G == 0):
            max_size = max(max_size, j-i)
        elif count_G > 0 and count_H > 0 and count_G == count_H:
            max_size = max(max_size, j-i)
 


print(max_size)