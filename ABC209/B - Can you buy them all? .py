









N,X = map(int,input().split())
A = list(map(int, input().split()))


c = N//2

a = sum(A)

d = a-c

if X>=d:
    print("Yes")
else:
    print("No")