






N = int(input())

X = 0
tmp = []

for i in range(N):
    A,B = map(int,input().split())
    X-=A
    tmp.append(A+A+B)

tmp.sort()
ans=0
while X<=0:
    X+= tmp.pop()
    ans+=1
print(ans)


