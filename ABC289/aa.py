




S = input()
s = list(S)
t = []

for i in range(len(s)):
    if s[i]=="0":
        t.append("1")
    else:
        t.append("0")
print("".join(t))
