










S = input()
S = list(S)
tmp = "atcoder"
tmp = list(tmp)

ans = 0
# aの場所チェック、1までの距離
# tの場所チェック、2までの距離
while True:
    if tmp ==S:
        print(ans)
        exit()
    a = S.index('a')
    ans +=a
    for i in range(a,0,-1):
        t = S[i]
        d = S[i-1]
        S[i] = d
        S[i-1] = t
    
    break
while True:
    if tmp ==S:
        print(ans)
        exit()
    a = S.index('t') 
    ans +=a-1
    for i in range(a,1,-1):
        t = S[i]
        d = S[i-1]
        S[i] = d
        S[i-1] = t
    
    break
while True:
    if tmp ==S:
        print(ans)
        exit()
    a = S.index('c') 
    ans +=a-2
    for i in range(a,2,-1):
        t = S[i]
        d = S[i-1]
        S[i] = d
        S[i-1] = t
   
    break
while True:
    if tmp ==S:
        print(ans)
        exit()
    a = S.index('o') 
    ans +=a-3
    for i in range(a,3,-1):
        t = S[i]
        d = S[i-1]
        S[i] = d
        S[i-1] = t
    
    break
    
while True:
    if tmp ==S:
        print(ans)
        exit()
    a = S.index('d') 
    ans +=a-4
    for i in range(a,4,-1):
        t = S[i]
        d = S[i-1]
        S[i] = d
        S[i-1] = t
   
    break
while True:
    if tmp ==S:
        print(ans)
        exit()
    a = S.index('e') 
    ans +=a-5
    for i in range(a,5,-1):
        t = S[i]
        d = S[i-1]
        S[i] = d
        S[i-1] = t
    
    break
while True:
    if tmp ==S:
        print(ans)
        exit()
    a = S.index('r') 
    ans +=a-6
    for i in range(a,6,-1):
        t = S[i]
        d = S[i-1]
        S[i] = d
        S[i-1] = t
    
    break