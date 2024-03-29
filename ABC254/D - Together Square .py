

N = int(input())

# 素因数分解
def prime_factorize(x):
    # もしx=1ならば
    if x==1:
        # 1を返す
        return [1]
    # 素因数を格納するリスト
    prime_list=[]
    # i=2,3,4,...で試し割り
    i=2
    # i<=√xすなわちi*i<=xの範囲で試し割り
    while i*i<=x:
        # もしiで割り切れたら
        if x%i==0:
            # iを素因数に追加
            prime_list.append(i)
            # xをiで割る
            x//=i
        # iで割り切れなかったら
        else:
            # 次のiへ
            i+=1
    # 試し割りが終わった時xが1でなければ
    if x!=1:
        # 素因数にxを追加
        prime_list.append(x)
    # 素因数のリストを返す
    return prime_list


if N==1:
    print(1)
    exit()
S = []
for i in range(N+1):
    S.append(i**2)

def f(j):
    ng = 0
    ok = N
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if j*S[mid]<=N:
            ng = mid
        else:
            ok = mid
    return ng

ans = 0

for i in range(1,N+1):
    j=1
    P = prime_factorize(i)
    p = set(P)
    for x in p:
        if P.count(x)%2==1:
            j*=x
    ans += f(j)


print(ans)