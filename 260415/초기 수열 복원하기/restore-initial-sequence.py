import sys

n = int(input())
adjacent = list(map(int, input().split()))

A = [0] * n



for i in range(1, n+1):
    A[0] = i
    
    for j in range(1, n):
        A[j] = adjacent[j-1] - A[j-1]

        satisfied = True
        exist = [False] * 1001
        for j in range(n):
            if A[j] <= 0 or A[j] > n:
                satisfied = False
            else:
                if exist[A[j]]:
                    satisfied = False
                exist[A[j]] = True
        if satisfied:
            for j in range(n):
                print(A[j], end=' ')
            sys.exit()

            

        
    

        
    
    
