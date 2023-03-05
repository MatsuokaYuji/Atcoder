











N = int(input())

import math

# s = 1 + isqrt(n - 1)
s = math.isqrt(N)

ans = 2*sum(N//i for  i in range(1,s+1)) -s*s
print(ans)