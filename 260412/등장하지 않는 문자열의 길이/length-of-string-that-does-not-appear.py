N = int(input())
str = input()

def count_chr(chr, k):
    count = 0
    for i in range(N - k + 1):
        if chr == str[i:i+k]:
            count += 1
    return count

min_len = 100

for k in range(1, N + 1):
    success = True
    for i in range(N - k + 1):
        chr = str[i:i+k]
        count = count_chr(chr, k)
        if count != 1:
            success = False
            break
    if success:
        min_len = min(min_len, k)
print(min_len)