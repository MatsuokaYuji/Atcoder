# O(logN)O(log⁡N) 	O(N)O(N)	O(N2)O(N2)	O(N3)O(N3)	O(2N)O(2N)
# 何でもあり	10^8 程度	10000 ～ 20000 程度	400 ～ 600 程度	20 ～ 25 程度

n, k = map(int,input().split())
A = list(map(int, input().split()))

# # すべてx以下の長さで切れるか判定
def afterdark(x):
    #切った個数
    cnt = 0
    for a in A:
        cnt+= a//x
        if a%x!=0:
          cnt+=1
        cnt-=1
    return cnt <= k

left = 0
right = max(A)

while abs(left - right)>1:
    mid = (left + right)//2
    if afterdark(mid):
        right = mid
    else:
        left = mid
print(right)

