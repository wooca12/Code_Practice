N = int(input())
str = input()

min_len = 100
for j in range(N):
    count = 0
    chr = str[:j+1]
    stop = False
    for k in range(N - len(chr) + 1):
        if chr == str[k: k + len(chr)]:
            count += 1
    if count == 1:
        min_len = min(min_len, len(chr))
print(min_len)
