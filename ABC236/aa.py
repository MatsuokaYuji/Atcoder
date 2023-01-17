



S = input()

S = list(S)
a,b = map(int,input().split())


tmp = S[a-1]
tmp1 = S[b-1]

S[a-1] = tmp1
S[b-1] = tmp

print("".join(S))
# for i in S:
#     print(i,end = "")