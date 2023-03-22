







N,M = map(int,input().split())


A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A+B

C.sort()

ans1 = []
ans2 = []
a = set(A)
b = set(B)

for i in range(len(C)):
    if C[i] in a:
        ans1.append(i+1)
    else:
        ans2.append(i+1)
print(*ans1)
print(*ans2)