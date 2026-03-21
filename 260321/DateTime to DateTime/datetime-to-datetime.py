a, b, c = map(int, input().split())

def num_minutes(a, b, c):
    total = a * 24 * 60 + b * 60 + c
    return total

diff = num_minutes(a, b, c) - num_minutes(11, 11, 11)
print(diff if diff >= 0 else -1)