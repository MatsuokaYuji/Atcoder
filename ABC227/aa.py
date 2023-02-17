

N,K,A = map(int,input().split())

n = [i for i in range(1,N +1)]
n = n+n

ans =  n[(K%N) + A-2]
# print(n)
print(ans)