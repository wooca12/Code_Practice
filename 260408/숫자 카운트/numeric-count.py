n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            
            succeeded = True
            for num, c1, c2 in arr:
                a = num // 100
                b = num // 10 % 10
                c = num % 10
                count1, count2 = 0, 0

                if a == i:
                    count1 += 1
                if a == j or a == k:
                    count2 += 1
                if b == j:
                    count1 += 1
                if b == i or b == k:
                    count2 += 1
                if c == k:
                    count1 += 1
                if c == i or c == j:
                    count2 += 1
                
                if count1 != c1 or count2 != c2:
                    succeeded = False
                    break
            if succeeded:
                count += 1

print(count)

            