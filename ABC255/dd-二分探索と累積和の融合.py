



from itertools import accumulate
import bisect

N,Q = map(int,input().split())

A =[0] + list(map(int, input().split()))

A.sort()

#累積和
sumA = list(accumulate(A))
# sumA = [0] + sumA


for i in range(Q):
    x = int(input())
    # 二分探索
    a = bisect.bisect(A,x) -1
    # print(a)
    ans = x*a -(sumA[a]) + (sumA[N]-sumA[a]) - x*(N-a)
    print(ans)
