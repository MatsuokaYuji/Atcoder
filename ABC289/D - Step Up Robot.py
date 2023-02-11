
import math
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

b = set(B)

X = int(input())
x = A[N-1]

# 今いる段にA[i]を使ってたどり着けるか？
dp = [False] *(10**5+1)

for i in range(N):
    if A[i] not in b:
        dp[A[i]] = True

for i in range(1,10**5+1):
    if i in b:
        continue
    for j in range(N):
        y = A[j]
        d = i - y
        if d<=0:
            continue
        if dp[d] == True:
            dp[i] = True

print("Yes" if dp[X] else "No")

