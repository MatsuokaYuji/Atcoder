



n = int(input())


A = []
B = set()
for i in range(n):
    flag = False
    s = input()
    A.append(s)
    B.add(s)
    if s[0] in ["H","D","C","S"]:
        if s[1] in ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]:
            if len(A)==len(B):
                flag = True
    if flag:
        continue
    else:
        break

if flag:
    print("Yes")
else:
    print("No")