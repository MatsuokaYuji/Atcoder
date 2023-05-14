








S = input()
s =list(S)
T = input()
t =list(T)
from collections import Counter
Cs=Counter(S)
Ct=Counter(T)

w = set(["a","t","c","o","d","e","r"])

# print(Cs)
# print(Ct)
Atcounts = Cs["@"]
Atcountt = Ct["@"]
# print(Atcounts, Atcountt)
Cs["@"] = Ct["@"]

d = Ct-Cs
# print(d)

e = Cs-Ct
# print(e)

scount = 0
tcount = 0
for i in d.items():
    if i[0] in w:
        scount+=i[1]
    else:
        print("No")
        exit()
for i in e.items():
    if i[0] in w:
        tcount+=i[1]
    else:
        print("No")
        exit()





if scount<=Atcounts and tcount <= Atcountt:
    print("Yes")
else:
    print("No")