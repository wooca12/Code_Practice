N = int(input())
numbers = list(map(int, input().split()))

group_nums = 0
odd = 0
even = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

while True:
    if even == 0 and odd == 0 :
        break

    if group_nums % 2 == 0: # 짝수 구해야함
        if even > 0:
            group_nums += 1
            even -= 1
        elif odd >= 2: # 짝수 없으면 홀수 2개 묶음
            odd -= 2
            group_nums += 1
        else: # 짝 구해야하지만 홀수 남을 때
             #  (짝수 A) + (홀수 B) + 홀수 C [현재 2]-> (짝수 A + 홀수 B + 홀수 C) [현재 1]
            # 마지막 홀수 그룹 없애고 짝수 그룹에 다 묶기
            if even > 0 or odd > 0:
                group_nums -= 1
            break

    
    else: # 홀수 구해야함
        if odd > 0:
            group_nums += 1
            odd -= 1
        else:
            #  (홀수 A) + (짝수 B) + 짝수 C [현재 2]-> (홀수 A) + (짝수 B + 짝수 C) [현재 2]
            # 마지막 짝수 그룹에 다 묶기
            break
print(group_nums)
        