





N = int(input())

S = input()
s = list(S)

A = [-1]*N

flag = True
count = 0 

for i in range(N):
    if S[i] == "," and flag:
        A[i] = 1
    if S[i] == '"' and count == 0:
        count = 1
        flag = False
    elif  S[i] == '"' and count == 1:
        count = 0
        flag = True

for i in range(N):
    if A[i] ==1:
        s[i] = "."
print("".join(s))
