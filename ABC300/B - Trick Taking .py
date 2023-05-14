




N,T = map(int,input().split())


C = list(map(int, input().split()))
R = list(map(int, input().split()))


s =set(C)  

tmp = 0
if T in s:
    for i in range(N):
        if C[i]==T:
            tmp = max(tmp,R[i])
    ans = R.index(tmp)
else:
    x = C[0]
    for i in range(N):
        if C[i]==x:
            tmp = max(tmp,R[i])
    ans = R.index(tmp)
print(ans+1)
