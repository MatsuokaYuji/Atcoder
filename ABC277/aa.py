n,x = map(int,input().split())



P = list(map(int, input().split()))


ans = 0
for i in range(n):
    if P[i] == x:
        ans = i+1

print(ans)