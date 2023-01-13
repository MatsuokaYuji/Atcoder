





from bisect import bisect_left, bisect_right


# 各数字がどこにあるか管理、二分探索でR,Lの位置を求める
N = int(input())

A = list(map(int, input().split()))

Q = int(input())

pos = [[] for i in range(N+1)]

for i,x in enumerate(A,1):
    pos[x].append(i)
# print(pos)

for i in range(Q):
    L,R,X = map(int,input().split())

    r = bisect_right(pos[X],R)
    l = bisect_left(pos[X],L)
    ans = r - l
    print(ans)
