

N = int(input())

S = input()
s = list(S)
flag = False
for i in range(N):
    if s[i]=="o":
        flag=True
    if s[i]=="x":
        print("No")
        exit()
if flag:
    print("Yes")
else:
    print("No")
