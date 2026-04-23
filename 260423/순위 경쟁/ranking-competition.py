n = int(input())
arr = []
for _ in range(n):
    ci, si = input().split()
    arr.append((ci, int(si)))

def get_winner(a, b, c):
    if a == b and b == c:  # A B C
        return 1   
    elif a == b and a > c:  # A B
        return 2
    elif b == c and a < c:  # B C
        return 3
    elif a == c and a < b: # A C
        return 4
    elif a > b and a > c: # A
        return 5
    elif b > a and b > c: # B
        return 6
    elif c > a and c > b: # C
        return 7

a, b, c = 0, 0, 0
cnt = 0
for person, score in arr:
    if person == 'A':
        if get_winner(a, b, c) != get_winner(a + score, b, c):
            a += score
            cnt += 1
    elif person == 'B':
        if get_winner(a, b, c) != get_winner(a, b + score, c):
            b += score
            cnt += 1
    elif person == 'C':
        if get_winner(a, b, c) != get_winner(a, b, c +score):
            c += score
            cnt += 1
print(cnt)