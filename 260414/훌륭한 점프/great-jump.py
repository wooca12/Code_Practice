n, k = map(int, input().split())
arr = list(map(int, input().split()))


minmax = 100

def is_possible(max_val):
    available_indices = []
    for i, elem in enumerate(arr):
        if elem <= max_val:
            available_indices.append(i)

    arr_size = len(available_indices)
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i-1]
        if dist > k:
            return False
    return True



for a in arr[1:n-1]:
    if is_possible(a):
        minmax = min(minmax, a)
print(minmax)