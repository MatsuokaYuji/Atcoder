






N,K = map(int,input().split())
A = list(map(int, input().split()))

if sum(A)<=K:
    ans = 0
    for a in A:
        ans+= a*(a+1)//2
    print(ans)
    exit()


def Nibutan(x):
    cnt =0
    for a in A:
        cnt += max(a-x+1,0)
    if cnt<=K:
        return True
    else:
        return False
left = 1
right = 10**20

while (right-left) >1:
    mid = (right+left)//2
    if Nibutan(mid):
        right = mid
    else:
        left = mid

ans = 0

for a in A:
    if right<=a:
        # rightより大きなカードをすべて取れる
        # a~rightまでの和を足す
        ans+=(a-right+1) * (a+right)//2
        K-=(a-right+1)
ans += (right-1) * K

print(ans)

