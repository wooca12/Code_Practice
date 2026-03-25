N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
punished_student = [0] * N



first_student = -1
for number in student:
    punished_student[number-1] += 1
    if punished_student[number - 1] >= K:
        first_student = number
        break
print(first_student)