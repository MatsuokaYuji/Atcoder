


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


N,M = map(int,input().split())
A = list(map(int, input().split()))

prime_set=set()


for x in A:
    if x==1:
        continue
    prime_x = prime_factorize(x)

    for p in prime_x:
        prime_set.add(p)

# ans_judge[x]=1なら答え、=0なら答えでない
ans_judge = [1] * (M+1)

for p in prime_set:
    # p*1,p*2,p*3,...,p*k,...は答えでない→ans_judge[p*k]=0とする
    # p*kがMを超えるまで
    k = 1
    while p*k<=M:
        ans_judge[p*k] = 0
        k+=1
ans = []

for i in range(1,M+1):
    if ans_judge[i]==1:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)