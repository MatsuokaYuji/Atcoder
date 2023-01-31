



N,Q = map(int,input().split())

_next = [-1] * (N+1)
_prev = [-1] * (N+1)


for i in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q==1:
        x,y = query[1],query[2]
        _next[x] = y
        _prev[y] = x
    elif q==2:
        x,y = query[1],query[2]
        _next[x] = -1
        _prev[y] = -1
    else:
        x = query[1]
        ans = []
        crr = x
        while _prev[crr] !=-1:
            crr = _prev[crr]
        while crr!=-1:
            ans.append(crr)
            crr = _next[crr]
        print(len(ans),*ans)
