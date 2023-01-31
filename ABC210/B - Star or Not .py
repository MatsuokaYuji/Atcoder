












N = int(input())
G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト

for i in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

for g in G:
    if len(g) == N-1:
        print("Yes")
        exit()
print("No")