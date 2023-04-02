






# def f(b):
#     return a*b
# # a をある値に固定したとき、
# # b をいくつにすれば X が M 以上で最小になるか
# for a in range(1,min(N+1,n+1)):
#     ng = -1
#     ok = N

#     while abs(ok-ng)>1:
#         mid = (ok+ng)//2
#         if f(mid)>=M:
#             ok = mid
#         else:
#             ng = mid
#     if f(ok)>=M:
#         ans = min(ans,f(ok))

N,M = map(int,input().split())

ans= float("INF")
for a in range(1,10**6+5):
    if M%a==0:
        b = M//a
    else:
        b =(M//a) +1
    if a<=N and b<=N:
        if a*b>=M:
            ans = min(ans,a*b)

if ans!=float("INF"):
    print(ans)
else:
    print(-1)
