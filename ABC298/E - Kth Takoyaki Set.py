







# import heapq
# N,K=map(int,input().split())
# A=list(map(int,input().split()))
# q=[0]
# prev=set()

# for _ in range(K+1):
#     a=heapq.heappop(q)
#     while a in prev:
#         a=heapq.heappop(q)
#     prev.add(a)
#     for i in A:
#         heapq.heappush(q,i+a)
#     print(q)
    

# print(a)


from heapq import heappop, heappush

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
q = [0]
seen = set()
while count <= K:
    x = heappop(q)
    if x not in seen:
        seen.add(x)
        count += 1
        for Ai in A:
            heappush(q, x+Ai)

print(x)