N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

max_count = 0

for i in range(N):
    tmp = [p for p in P]
    tmp[i] //= 2
    price_list = [tmp[a] + S[a] for a in range(N)] 
    price_list.sort()

    price, count = 0, 0
    
    for j in range(N):
        price += price_list[j]
        if price <= B:
            count += 1
    max_count = max(max_count, count)

print(max_count)
        
        