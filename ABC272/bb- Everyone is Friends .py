


N,M= map(int,input().split())


A = [list(map(int, input().split())) for _ in range(M)]

# l.pop(0)

for k in range(M):
    A[k].pop(0)
# x=A[1:] ともかけた


for i in range(N-1):
    for j in range(i+1,N):
        flag = False
        for k in range(M):
            if i+1 in A[k] and j+1 in A[k]:
                flag =True
                continue
        if not flag:
            print("No")
            exit()

print("Yes")
                    
