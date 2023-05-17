



N = int(input())
A = list(map(int, input().split()))


from collections import defaultdict
d = defaultdict(int)


for i in range(N-1):
    a = A[i]
    d[a]+=1
# print(d)
for i in range(N):
    print(d[i+1])
