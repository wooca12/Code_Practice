a, b, c, d = map(int, input().split())

# 0 1 2 3 4 5 6 7 8 9 10 11 12
months = [0, 31 , 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_days = 0
for m in range(a, c):
    total_days += months[m]

total_days = total_days - b + d + 1
print(total_days)