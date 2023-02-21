


N = int(input())
A = list(map(int, input().split()))


# N <=10**4なのでN**2が間に合う。
# 区間の最小値求めるのは今の最小値と追加する要素で行えばO(1)
ans = 0
for l in range(N):
    tmp = 10**5+1
    for r in range(l,N):
        length = r-l+1
        tmp = min(tmp,A[r])
        kk = tmp * length
        ans = max(ans,kk)
print(ans)