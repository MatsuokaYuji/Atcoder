




N,Q = map(int,input().split())

S = input()

c = 0

for _ in range(Q):
        query = list(map(int, input().split()))
        t = query[0]
        if t == 1:
            x = query[1]
            c = (c-x)%N
        elif t == 2:
            x = query[1]
            a = (c + x-1)%N
            print(S[a])
