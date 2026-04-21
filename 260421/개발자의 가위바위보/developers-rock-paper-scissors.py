N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]

def first_win(dic):
    cnt = 0
    for p1, p2 in moves:
        if dic[p1] == '가위' and dic[p2] == '보':
            cnt += 1
        elif dic[p1] == '바위' and dic[p2] == '가위':
            cnt += 1
        elif dic[p1] == '보' and dic[p2] == '바위':
            cnt += 1

    return cnt

maxcnt = first_win({1:'가위', 2:'바위', 3:'보'})
maxcnt = max(maxcnt, first_win({1:'가위', 2:'보', 3:'바위'}))   
maxcnt = max(maxcnt, first_win({1:'바위', 2:'가위', 3:'보'}))   
maxcnt = max(maxcnt, first_win({1:'바위', 2:'보', 3:'가위'}))   
maxcnt = max(maxcnt, first_win({1:'보', 2:'가위', 3:'바위'}))   
maxcnt = max(maxcnt, first_win({1:'보', 2:'바위', 3:'가위'}))   

print(maxcnt)