m1, d1, m2, d2 = map(int, input().split())
A = input()

month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_weekend = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def num_days(month, day):
    total = 0
    for m in range(1, month):
        total += month_days[m]
    return total + day - 1

diff = num_days(m2, d2) - num_days(m1, d1)
num_week = diff // 7
weekend = day_weekend[diff % 7]
count = 0


count += num_week
if weekend == A:
    count += 1

print(count)