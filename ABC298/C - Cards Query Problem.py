
N = int(input())
Q = int(input())
from collections import defaultdict


queries = [ list(map(int, input().split())) for i in range(Q) ]

boxes=defaultdict(list)
num=defaultdict(set)
for t in queries:
    tp =t[0]
    if tp == 1:
        # i = t[1]
        # j = t[2]
        i,j = t[1:]
        num[i].add(j)
        boxes[j].append(i)
    if tp == 2:
        i = t[1]
        print(*(sorted(boxes[i])))
        
    if tp ==3:
        i = t[1]
        print(*(sorted(num[i])))

# n = int(input())
# q = int(input())
# ls = [[] for _ in range(n)]
# b = [[] for _ in range(2*10**5+1)]
# for _ in range(q):
#   query = list(map(int, input().split()))
#   if query[0] == 1:
#     i, j = query[1:]
#     ls[j-1].append(i)
#     b[i].append(j)
#   elif query[0] == 2:
#     i = query[1] - 1
#     ls[i].sort()
#     print(*ls[i])
#   else:
#     i = query[1]
#     b[i] = list(set(b[i]))
#     b[i].sort()
#     print(*b[i])


# N = int(input())
# Q = int(input())
# M = 200001
# box = [[] for _ in range(N + 1)]
# card = [set() for _ in range(M)]
# for _ in range(Q):
#     q = list(map(int, input().split()))
#     if q[0] == 1:
#         i, j = q[1:]
#         box[j].append(i)
#         card[i].add(j)
#     elif q[0] == 2:
#         print(' '.join(map(str, sorted(box[q[1]]))))
#     else:
#         print(' '.join(map(str, sorted(card[q[1]]))))