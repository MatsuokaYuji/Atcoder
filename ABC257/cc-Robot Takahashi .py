


N = int(input())
S = input()


W = list(map(int, input().split()))

L = []

for w,s in zip(W,S):
    L.append([w,int(s)])
L.sort()

tmp = S.count("1")
max_tmp = tmp

adult,child = 0,0

for i in range(1,len(L)):
    if L[i][0] == L[i-1][0]:
        if L[i-1][1]==1:
            adult+=1
        if L[i-1][1]==0:
            child+=1
    else:
        if L[i-1][1]==1:
            tmp += (child - adult - 1)
        if L[i-1][1]==0:
            tmp += (child - adult + 1)
        adult,child = 0,0
        if max_tmp< tmp:
            max_tmp = tmp
print(max(max_tmp,S.count("0")))