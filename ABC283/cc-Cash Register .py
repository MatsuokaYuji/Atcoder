



S = input()


cnt = 0

while len(S) > 0:
    t = len(S)
    if t>=2:
        if S[-1] == "0" and S[-2]=="0":
            S = S[:-2]
            cnt+=1
        elif S[-2]=="0":
            S = S[:-1]
            cnt+=1
        else:
            S = S[:-1]
            cnt+=1
    if t==1:
        cnt+=1
        print(cnt)
        exit()
