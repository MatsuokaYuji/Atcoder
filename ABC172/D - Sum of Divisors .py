




N = int(input())

ans = 0


# 表で考える、整数問題、縦から見る

for a in range(1,N+1):
    tmp = N//a
    for b in range(1,tmp+1):
        x = a*b
        ans+=x
print(ans)
