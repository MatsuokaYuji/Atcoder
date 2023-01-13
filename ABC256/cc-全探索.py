



h1,h2,h3,w1,w2,w3 = map(int,input().split())


ans = 0
for a1 in range(1,29):
    for a2 in range(1,29):
        a3 = h1-a1-a2
        if a3>=1 and a3<=28:
            for b1 in range(1,29):
                for b2 in range(1,29):
                    b3 = h2-b1-b2
                    if b3>=1 and b3<=28:
                        #最終段チェック
                        c1 = w1-a1-b1
                        if c1>=1 and c1<=28:
                            c2 = w2-a2-b2
                            if c2>=1 and c2<=28:
                                c3 = w3-a3-b3
                                if c3>=1 and c3<=28 and h3 == c1+c2+c3:
                                    ans+=1
print(ans)