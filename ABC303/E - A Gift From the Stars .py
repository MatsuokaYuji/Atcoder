



N=int(input())

eds=[set() for _ in range(N)]

jisu = [0]*N

for _ in range(N-1):
  u,v=map(int,input().split())
  u-=1 ; v-=1
  eds[u].add(v) ; jisu[u]+=1
  eds[v].add(u) ; jisu[v]+=1

ans=[]
seen=[0]*N

for i in range(N):
    if jisu[i]>=3:
        ans.append(jisu[i])
        seen[i] = 1
        for j in eds[i]: seen[j] = 1
for _ in range(seen.count(0)//3):
    ans.append(2)
# print(seen)
print(*sorted(ans))