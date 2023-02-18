





import sys
sys.setrecursionlimit(10**9)

# 再帰
N,K = map(int,input().split())
A = list(map(int, input().split()))

def calc(n):
    num = 0
    for i in A:
        num+=min(i,n)
    return num

left = 0
right = 10**12

while left+1<right:
    mid = (left + right)//2
    if calc(mid)<=K:
        left = mid
    else:
        right = mid

# left何周、done何個取り除いたか
done = calc(left)
# print(done)

for i in range(N):
    if K-done ==0:
        break
    if A[i] - left>0:
        A[i]-=1
        done+=1
for i in range(N):
    print(max(0,A[i]-left),end=" ")

