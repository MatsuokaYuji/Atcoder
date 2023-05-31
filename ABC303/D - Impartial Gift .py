

N,M,D = map(int,input().split())


A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
# from bisect import bisect_left,bisect


# for i in range(N):
#     a = A[i]
#     sub1 = a+D
#     sub2 = a-D
#     kouho1 = bisect_left(B,sub1)
#     kouho2 = bisect_left(B,sub2)
#     print(kouho1,kouho2)


a = A[0]
b = B[0]



if a>=b:
    start = a
    ban = "a"
else:
    start = b
    ban = "b"

apos = 0
bpos = 0
while True:
    if ban == "a":
        a = A[apos]
        b = B[bpos]
        d = abs(start-B[bpos])
        if d<=D:
            print(a+b)
            exit()
        apos+=1
        if apos == N:
            print(-1)
            exit()
        if A[apos] >=B[bpos]:
            start = A[apos]
        else:
            start = B[bpos]
            ban = "b"
    else:
        a = A[apos]
        b = B[bpos]
        d = abs(start-A[apos])
        if d<=D:
            print(a+b)
            exit()
        bpos+=1
        if bpos == M:
            print(-1)
            exit()
        if A[apos] >=B[bpos]:
            start = A[apos]
            ban = "a"
        else:
            start = B[bpos]
            ban = "b"





