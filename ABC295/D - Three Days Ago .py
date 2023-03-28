
# from collections import defaultdict
# import math

# def comb(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
 
# s = input()
# n = len(s)

# cnt = [0]*10
# d = defaultdict(int)
# d[tuple(cnt)] +=1

# for i in range(n):
#     t = int(s[i])
#     cnt[t] = (cnt[t]+1)%2
#     # print(cnt)
#     d[tuple(cnt)] +=1
# # print(d)

# ans = 0

# for v in d.values():
#     if v>=2:
#         ans+=comb(v,2)
# print(ans)


from collections import defaultdict
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
 
s = input()
n = len(s)

cnt = [0] * 10
d = defaultdict(int)
d[tuple(cnt)] +=1

for i in range(n):
    x = int(s[i])
    cnt[x] +=1
    cnt[x] %=2
    d[tuple(cnt)] +=1

ans =0
for v in d.values():
    if v>=2:
        ans+=comb(v,2)
print(ans)

