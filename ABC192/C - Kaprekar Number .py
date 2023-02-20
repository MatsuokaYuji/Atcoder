











N,K = map(int,input().split())

a = N
for i in range(K):
    a1 = str(a)
    a2 = str(a)
    g1 = list(a1)
    g2 = list(a2)
    g1.sort(reverse=True)
    g2.sort()
    d1 = int("".join(g1))
    d2 = 0
    for i in range(len(g2)):
        x = g2[i]
        if x !="0":
            tmp = int(x) * (10**(len(g2)-i-1))
            d2+=tmp
    a = d1-d2
print(a)
