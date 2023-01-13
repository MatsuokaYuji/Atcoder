







h,w = map(int,input().split())

ans = 0
for i in range(h):
    s = input()
    t = s.count("#")
    ans+=t
print(ans)