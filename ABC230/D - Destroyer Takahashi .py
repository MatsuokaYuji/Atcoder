


from operator import itemgetter

N,D = map(int,input().split())

A = [] * N

for i in range(N):
    l,r = map(int,input().split())
    A.append([l,r])
# print(A)
A = sorted(A, key = itemgetter(1))
# print(A)

ans = 0
x = 0
# Riでソート
# Riから+D-1までをxとして、Li<xかを判定

for l,r in A:
    if x<l:
        ans+=1
        x = r + D-1
print(ans)



