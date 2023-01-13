





n,m = map(int,input().split())




A = [list(input().split()) for _ in range(n)]


ans = 0

for i in range(n-1):
    for j in range(i+1,n):
        flag = True
        for k in range(m):
            
            if A[i][0][k]=="x" and A[j][0][k] == "x":
                flag = False
                continue
        if flag:
            ans+=1

print(ans)