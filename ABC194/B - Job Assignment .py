





N = int(input())

time = []

for i in range(N):
    A,B = map(int,input().split())
    time.append(A,B)


ans = 10*10**11

for i in range(N):
    for j in range(N):
        if i != j:
            tmp = max(time[i][0],time[j][1])
        else:
            tmp = time[i][0] + time[j][1]
        ans = min(ans,tmp)
print(ans)
