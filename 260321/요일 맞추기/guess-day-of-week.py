m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekend = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun' ]

def num_days(m, d):
    total_days = 0
    for i in range(1, m):
        total_days += months[i]
    return total_days + d
total = d2 - d1

diff = num_days(m2, d2) - num_days(m1, d1)

w = diff % 7
print(weekend[w])