



S = input()
s = list(S)


c = []
k = []
r = []

for i in range(len(s)):
    if s[i]=="B":
        c.append(i)
    if s[i]=="K":
        k.append(i)
    if s[i]=="R":
        r.append(i)
    
if c[0]%2==c[1]%2:
    print("No")
    exit()
# print(k,r)
if not(r[0]<k[0]<r[1]):
    print("No")
    exit()
print("Yes")
