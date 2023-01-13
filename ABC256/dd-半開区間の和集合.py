


n = int(input())

lr = []
for i in range(n):
    l,r = map(int,input().split())
    lr.append([l,"left"])
    lr.append([r,"right"])
lr.sort()


ans = []
cnt = 0
for v,x in lr:
    if x == "left":
        cnt += 1
        if cnt ==1:
            ans.append(v)
    if x == "right":
        cnt-=1
        if cnt==0:
            ans.append(v)

for i in range(len(ans)//2):
    print(ans[2*i],ans[2*i+1])