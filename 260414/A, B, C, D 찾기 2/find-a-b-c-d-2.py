import sys
nums = list(map(int, input().split()))

def is_correct(a, b, c, d):
    arr = [a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d]
    nums.sort()
    arr.sort()
    
    for n, a in zip(nums, arr):
        if n != a:
            return False
    return True

for a in range(1, 40):
    for b in range(a, 40):
        for c in range(b, 40):
            for d in range(c, 40):
                if is_correct(a,b,c,d):
                    print(a,b,c,d)
                
                

                