a, b, x, y = map(int, input().split())

plan1 = abs(a - b)
plan2 = abs(a - x) + abs(b - y)
plan3 = abs(a - y) + abs(b - x)
print(min(plan1, plan2, plan3))