n = int(input())
S = input()

count = 0
length = len(S)

for i in range(length):
    if S[i] == 'C':
        for j in range(i + 1, length):
            if S[j] == 'O':
                for j in range(j + 1, length):
                    if S[j] == 'W':
                        count += 1
print(count)