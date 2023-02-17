












N = int(input())
S = input()
Q = int(input())

s = list(S)
x = s[:N]
y = s[N:]
L = [x,y]
def get(x):
    if x < N:
        return 0,x
    else:
        return 1, x-N


for i in range(Q):
    t,a,b = map(int,input().split())
    a-=1
    b-=1
    if t == 1:
        ai,aj = get(a)
        bi,bj = get(b)
        L[ai][aj],L[bi][bj] = L[bi][bj],L[ai][aj]
        
    if t == 2:
        L[0],L[1] = L[1],L[0]
        
ans = "".join(L[0]) + "".join(L[1])
print(ans)
