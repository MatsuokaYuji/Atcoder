









A,B,C,X = map(int,input().split())

if A>=X:
    print(1)
    exit()
if B<X:
    print(0)
    exit()
d = B-A
ans = C/d

print(ans)