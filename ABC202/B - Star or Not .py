





















S = input()

S = list(S)
S.reverse()
S = "".join(S)
ans = []

for i in S:
    if i=="6":
        ans.append("9")
        continue
    if i=="9":
        ans.append("6")
        continue    
    ans.append(i)   
print("".join(ans))