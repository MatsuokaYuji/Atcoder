









K = int(input())

ans = 0
c = 0
# 余りは高々K種類(0~K-1)
for i in range(1,10**6+5):
    c*=10
    c+=7
    c%=K
    if c==0:
        print(i)
        exit()
print(-1)