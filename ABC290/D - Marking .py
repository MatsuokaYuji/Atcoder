



import math
T = int(input())

for i in range(T):
    n,d,k = map(int,input().split())
    loop_count = n//math.gcd(n,d)
    ans = ((k-1)%loop_count*d)%n + (k-1)//loop_count
    print(ans)
