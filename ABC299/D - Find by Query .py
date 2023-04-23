








# import math
# N = int(input())
# ans = 1
# from collections import defaultdict
# d = defaultdict(int)
# for i in range(N):
#     d[i+1] = -1
# d[0] =-1
# d[1] = 0
# d[N] = 1
# d[N+1] = -1

# x = (N//2) 
# from collections import deque
# q = deque()

# while q:
#     print("?", x, flush=True)
#     i = int(input())
#     d[x] = i
#     if d[x-1]!=-1 and 1<=x<=N-1:
#         if i!=d[x-1]:
#             print("!", x,flush=True)
#             exit()
#     if d[x+1]!=-1 and 1<=x<=N-1:
#         if i!=d[x+1]:
#             print("!", x,flush=True)
#             exit()
#     if i==1:
#         x = (x//2)
#         y = x+1
#         q.append(x)
#         q.append(y)
#     else:
#         x = x + ((N-x)//2) 
#         y = x+1
#         q.append(x)
#         q.append(y)
#     if x == 1 or x == N-1:
#         x = q.popleft()
#         continue


n = int(input())
l = 1
r = n

while r - l > 1:
    mid = (l + r) // 2
    print('?', mid, flush=True)
    res = int(input())
    if res == 1:
        r = mid
    else:
        l = mid


print("!", l)




    