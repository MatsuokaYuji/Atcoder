










N, M = map(int, input().split())
A = list(map(int, input().split()))

z = N-sum(A)

print(z if z>=0 else -1)