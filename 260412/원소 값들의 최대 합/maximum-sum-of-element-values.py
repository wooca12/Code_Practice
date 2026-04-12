n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_sum = 0
for i in range(n):
    move = arr[i] 
    move_sum = 0
    for _ in range(m): # 2 3
        move_sum += arr[move] # 4 + 2
        move = arr[move] - 1 # 3 1

    max_sum = max(max_sum, move_sum)
print(max_sum)
