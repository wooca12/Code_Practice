a, b = map(int, input().split())
n = input()

num = 0
for i in range(len(n)):
    num = num * a + int(n[i])

digit = []
while True:
    if num < b:
        digit.append(num)
        break
    digit.append(num % b)
    num = num // b

for i in digit[::-1]:
    print(i, end='')