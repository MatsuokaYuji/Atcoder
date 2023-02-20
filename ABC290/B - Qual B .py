







N,K = map(int,input().split())
S = input()
S = list(S)

ans = []

count = 0
for i in range(len(S)):
    if S[i] == "o" and count<K:
        ans.append(S[i])
        count+=1
    else:
        ans.append("x")
print("".join(ans))
