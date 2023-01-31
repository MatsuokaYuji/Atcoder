






N,X = map(int,input().split())


money= set()
money.add(0)

for i in range(N):
    a,b = map(int,input().split())
    tmp=set()
    for each in money:
        for i in range(b+1):
            if X>=a*i + each:
                tmp.add(a*i + each)
    money = tmp
if X in money:
    print("Yes")
else:
    print("No")
