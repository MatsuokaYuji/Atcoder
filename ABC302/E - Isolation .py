


N, Q = map(int, input().split())
queries = [ list(map(int, input().split())) for i in range(Q) ]

eds=[set() for _ in range(N)]

ans = N
for q in queries:
    if q[0] == 1:
        u,v = q[1],q[2]
        u-=1
        v-=1
        if len(eds[u])==0:
            ans-=1
        if len(eds[v])==0:
            ans-=1
        eds[u].add(v)
        eds[v].add(u)
    if q[0] == 2:
        v = q[1]
        v-=1
        if len(eds[v])!=0:
            for j in eds[v]:
                eds[j].discard(v)
                if len(eds[j]) == 0:
                    ans+=1
            #setを空に初期化する
            eds[v].clear()
            ans+=1
    print(ans)

        