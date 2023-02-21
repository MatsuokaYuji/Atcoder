



import math
T = int(input())

for i in range(T):
    n,d,k = map(int,input().split())
    loop_count = n//math.gcd(n,d)
    ans = ((k-1)%loop_count*d)%n + (k-1)//loop_count
    print(ans)


# import sys
# readline = sys.stdin.readline

# import math
# def lcd(x, y):
#   return x // math.gcd(x,y) * y
  
# T = int(readline())
# for _ in range(T):
#   N,D,K = map(int,readline().split())
#   one_loop = lcd(N, D) // D
#   start = (K - 1) // one_loop
#   rest = (K - 1) % one_loop
#   ans = (start + rest * D) % N
#   print(ans)