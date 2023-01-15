


N = int(input())


A = list(map(int, input().split()))

# iこめ入れた時にそのiを記録かつ何連続しているかを記録

L = [[-1,0]]
ans=0
for cx in A:
    tx,cnt = L[-1]
    ans+=1
    if tx == cx:
        L[-1][1]+=1
    else:
        L.append([cx,1])
    if L[-1][0] == L[-1][-1]:
        L.pop()
        ans-=cx
    print(ans)
