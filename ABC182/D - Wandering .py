








from itertools import accumulate

# 累積和と正の整数の地点をまとめる
N = int(input())
A = list(map(int, input().split()))

B = list(accumulate(A))
q = [0] *(N)
for i in range(N):
    if i == 0:
        q[0] = max(0,B[0])
        continue
    q[i] = max(q[i-1],B[i])
    
# print(B)
# print(q)

ans = 0
x = 0
for i in range(len(B)):
    ans = max(ans,x+q[i])
    x = x + B[i]
print(ans)