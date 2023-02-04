



n,m = map(int,input().split())

A = list(map(int, input().split()))

B = set(A)
ans = sum(A)
for a in A:
    tmp = (a+1) %m
    B.add(tmp)

print(A)
A.sort()
print(A)
print(B)
print(ans)
# [18, 16, 15, 9, 8, 8, 17, 1, 3, 17, 11, 9, 12, 11, 7, 3, 2, 14, 3, 12]
