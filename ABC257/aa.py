






import string

n,x = map(int,input().split())


d = string.ascii_uppercase

s = ""

for i in range(26):
    for j in range(n):
        s+=d[i]
print(s[x-1])
