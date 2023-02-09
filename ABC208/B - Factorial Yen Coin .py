


def kai(x):
    if x ==1:
        return x
    return x * kai(x-1)





P = int(input())

ans = 0
for i in range(10,0,-1):
    d = kai(i)
    while P>=d:
        P-=d
        ans+=1
    if P==0:
        break
print(ans)

