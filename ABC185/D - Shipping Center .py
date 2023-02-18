




n,m,q = map(int,input().split())


item = []
for i in range(n):
    w, v = map(int, input().split())
    # vでソート、価値高い順
    item.append((v,w))

item.sort(reverse=True)
x = list(map(int, input().split()))


def solve(x):
    # 箱は小さい順
    x.sort()
    N = len(x)
    used = [False] * N
    ans = 0
    for (v,w) in item:
        for j in range(N):
            if used[j]:continue
            if x[j]<w:continue
            else:
                ans+=v
                used[j] = True
                break
    return ans


for _ in range(q):
    l,r = map(int,input().split())
    ans = solve(x[:l-1] + x[r:])
    # print(x[:l-1] + x[r:])
    print(ans)
