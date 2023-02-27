




N,C = map(int,input().split())


item = []
for i in range(N):
    a,b,c = map(int, input().split())
    a-=1
    item.append((a,c))
    item.append((b,-c))

item.sort()

ans = 0
fee = 0
t = 0

for x,y in item:
    if x !=t:
        ans+= min(C,fee) * (x-t)
        t = x
    fee+=y
print(ans)
