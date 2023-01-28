




from operator import itemgetter



N,W = map(int,input().split())

AB = [list(map(int,input().split())) for i in range(N)]

AB.sort( key = itemgetter(0),reverse=True)

ans = 0
tmp = W

for a,b in AB:
    if tmp == 0:
        print(ans)
        exit()
    if b>tmp:
        ans+= a*tmp
        print(ans)
        exit()
    else:
        ans+= a*b
        tmp-= b
print(ans)

