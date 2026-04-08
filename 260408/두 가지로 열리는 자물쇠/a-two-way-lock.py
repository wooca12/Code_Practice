N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

count = 0
same = 0

def condition_num(num):
    arr = []
    for n in range(1, N+1):
        diff = abs(num - n)
        if diff <= 2 or diff >= N - 2:
            arr.append(n)
    return arr

def same_num(arr1, arr2):
    count = 0
    for i in arr1:
        if i in arr2:
            count += 1
    return count

a1_ns = condition_num(a1)
a2_ns = condition_num(a2)
b1_ns = condition_num(b1)
b2_ns = condition_num(b2)
c1_ns = condition_num(c1)
c2_ns = condition_num(c2)

a3 = same_num(a1_ns, a2_ns)
b3 = same_num(b1_ns, b2_ns)
c3 = same_num(c1_ns, c2_ns)

count = len(a1_ns) * len(b1_ns) * len(c1_ns) + len(a2_ns) * len(b2_ns) * len(c2_ns) - a3 * b3 * c3

print(count)

            


