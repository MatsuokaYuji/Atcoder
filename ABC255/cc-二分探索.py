


X,A,D,N = map(int,input().split())


# Min = min(A,A+D*(N-1))
# Max = max(A,A+D*(N-1))

# if X<=Min:
#     print(Min-X)
# elif X >=Max:
#     print(X-Max)
# else:
#     tmp = abs(X-A)
#     c = tmp % abs(D)
#     if c <= abs(D/2):
#         print(c)
#     else:
#         print(abs(c-abs(D)))




# DがPlusの場合だけの解き方
def S(i):
    return A +(i-1)*D

def NibutanPlus(X):
    l = 0
    r = N
    while 1<r-l:
        c = (l+r)//2
        if S(c) <= X:
            l = c
        else:
            r =c
    return l,r
if X<A:
        # (A-X)が答え
        print(A-X)
    # Xが末項より大きい場合
elif S(N)<=X:
    # (X-末項)が答え
    print(X-S(N))
else:
    l,r = NibutanPlus(X)
    print(min(X-S(l),S(r)-X))