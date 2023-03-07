





N,X = map(int,input().split())

S = input()

s = list(S)

ans = X
for i in s:
    if i=="o":
        ans+=1
    if i=="x" and ans>=1:
        ans-=1
print(ans)
