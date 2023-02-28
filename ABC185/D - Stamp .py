




N,M = map(int,input().split())
if M==0:
    print(1)
    exit()

A = list(map(int, input().split()))

A.append(0)
A.sort()
A.append(N+1)
L = []

for i in range(len(A)-1):
    x = A[i+1] -A[i] -1
    L.append(x)

L.sort(reverse=True)

while (len(L))>0 and L[-1] == 0:
    L.pop()
if len(L) == 0:
    print(0)
    exit()


k = min(L)
# print(k)
ans = 0

for i in L:
    if i%k==0:
        tmp = i//k
        ans+=tmp
    else:
        tmp = (i//k) +1
        ans+=tmp
print(ans)
