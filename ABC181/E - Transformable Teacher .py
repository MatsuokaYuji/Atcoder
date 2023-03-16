





from bisect import bisect_left,bisect

N,M = map(int,input().split())
A = list(map(int, input().split()))
A.sort()
W = list(map(int, input().split()))

ans = float("INF")

left = [0] *(N+1)
right = [0] *(N+1)

for i in range(2,N,2):
  left[i] = left[i-2] + A[i-1] -A[i-2]
  right[i] = right[i-2] + A[N-i+1] - A[N-i]

for i in range(M):
  tmp  = W[i] 
  x = bisect_left(A,tmp)
#   print(x)
  if x%2==0:
    ans = min(ans,left[x] + right[N-x-1] + A[x]-tmp)
  else:
    ans = min(ans,left[x-1] + right[N-x] + tmp -A[x-1])
print(ans)
