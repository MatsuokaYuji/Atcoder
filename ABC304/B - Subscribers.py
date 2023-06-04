






N = int(input())


for i in range(3,10):
    if N<=10**i-1:
        N = str(N)
        l = len(N)
        m = l-(i-3)
        # print(N,i)
        ans = N[:m]
        for i in range(i-3):
            ans+="0"
        print(ans)
        exit()