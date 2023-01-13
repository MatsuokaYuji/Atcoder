





a, b = map(int,input().split())


ans = float(b)/float(a)

m = round(ans, 3) 

l = str(m)
tmp = 0

if len(l) != 5:
    tmp = 5-len(l) 
for i in range(tmp):
    l = l + "0"

print(l)
