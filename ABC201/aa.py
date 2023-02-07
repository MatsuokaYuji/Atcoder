




A = list(map(int, input().split()))


A.sort()

x = A[2]-A[1]
y = A[1]-A[0]
if x-y == 0:
    print("Yes")
else:
    print("No")
