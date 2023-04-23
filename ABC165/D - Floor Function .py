





A,B,N = map(int,input().split())



x = min(N,B-1)

ans = (A*x)//B -A*(x//B)
print(ans)