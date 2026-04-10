k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

rank = []
contest = arr[0]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if contest[i] < contest[j]:
            rank.append((i, j))
                
for i in range(1, k):
    contest = arr[i]
    new_rank = []
    for j in range(len(rank)):
        a, b = rank[j][0], rank[j][1]
        if contest[a] < contest[b]:
            new_rank.append((a,b))
    rank = new_rank
            

print(len(rank))