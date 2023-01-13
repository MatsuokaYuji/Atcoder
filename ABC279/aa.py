






S = input()

l = len(S)

ans=0
for i in range(l):
    if S[i] == "v":
        ans+=1
    else:
        ans+=2
print(ans)