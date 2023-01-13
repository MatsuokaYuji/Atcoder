
N,M,T = map(int,input().split())


A = list(map(int, input().split()))


Y = [ list(map(int, input().split())) for i in range(M) ]



count = [0] * (N + 1)
for i in Y:
    count[i[0]] = i[1]
# print(count)


for i in range(N-1):
    T = T - A[i]
    if T<=0:
        print("No")
        exit()
    T+=count[i+2]
print("Yes")
    
