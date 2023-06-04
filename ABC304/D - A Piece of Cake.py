








w,h = map(int,input().split())
N = int(input())

z = []
for i in range(N):
    p,q = map(int,input().split())
    z.append((p,q))
z.sort()
# print(z)
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))
m = (A+1)*(B+1)

from bisect import bisect_left,bisect
from collections import defaultdict
ans = defaultdict(int)

for i in range(N):
    x,y = z[i]
    s = bisect_left(a,x)
    t = bisect_left(b,y)
    # この書き方ができることを覚える
    ans[(s,t)]+=1
maxim = max(ans.values())
minim = min(ans.values())
if m != len(ans):
    minim = 0

print(minim, maxim)



# # 
# from bisect import bisect, bisect_left
# from collections import defaultdict

# W, H = map(int, input().split())
# N = int(input())
# p = [list(tuple(map(int, input().split()))) for _ in range(N)]
# a_n = int(input())
# a = list(map(int, input().split()))
# b_n = int(input())
# b = list(map(int, input().split()))

# ans = defaultdict(int)

# for i in range(N):
#     x, y = p[i][0], p[i][1]
#     ind_a = bisect(a, x)
#     ind_b = bisect(b, y)
#     #print(ind_a, ind_b)
#     ans[(ind_a, ind_b)] += 1
    
# maxim = max(ans.values())
# minim = min(ans.values())
# if (a_n+1)*(b_n+1) != len(ans):
#     minim = 0

# print(minim, maxim)
