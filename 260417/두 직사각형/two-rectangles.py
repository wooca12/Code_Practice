x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

def overlapping(arr1, arr2):
    if arr1[1] > arr2[3] or arr2[1] > arr1[3] :
        return False
    elif arr1[0] > arr2[2] or arr2[0] > arr1[2]:
        return False
    return True

if overlapping([x1, y1, x2, y2], [a1, b1, a2, b2]):
    print("overlapping")
else:
    print("nonoverlapping")