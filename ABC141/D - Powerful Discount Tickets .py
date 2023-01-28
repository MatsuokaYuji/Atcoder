







N,M= map(int,input().split())
A = list(map(int, input().split()))
from heapq import heapify,heappop,heappush
a = list(map(lambda x: x*(-1), A))

heapify(a)

for i in range(M):
    max_value = heappop(a)*(-1)
    heappush(a,(max_value)//2*(-1))

print((-1) * sum(a))
