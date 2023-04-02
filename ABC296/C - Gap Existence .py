






N,X = map(int,input().split())
A = list(map(int, input().split()))


A.sort()

B = set()

for i in A:
    d = i+X
    B.add(d)

for i in A:
    if i in B:
        print("Yes")
        exit()
print("No")