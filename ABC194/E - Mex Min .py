




from collections import Counter

N,M = map(int,input().split())
A = list(map(int, input().split()))

C = Counter(A[:M])

ans = 10**7

def mex(C):
    for i in range(N+1):
        if C[i] == 0:
            return i

ans = min(ans,mex(C))
mincount = 0

for i in range(N-M):
    C[A[i]] -=1
    C[A[i+M]] +=1
    if A[i] < ans and C[A[i]] == 0:
        ans = A[i]
    # elif C[ans] == 0:
    #     continue
print(ans)

