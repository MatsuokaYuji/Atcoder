

N = int(input())
A = [0] * (2*N)
for i in range(2*N-1):
    A[i] = list(map(int, input().split()))

ans = 0

def calc(dancer, score):
    if len(dancer) == 0:
        global ans
        ans = max(ans, score)
        return
    last = dancer[-1]
    for i in range(len(dancer)-1):
        # print(dancer[:i] + dancer[i+1:-1])
        other = dancer[i]
        calc(dancer[:i] + dancer[i+1:-1], score ^ A[other][last-other-1])


calc(list(range(2*N)), 0)
print(ans)
        

    




# # 16!//2**8//8!通りなので全探索が可能

# import sys
# sys.setrecursionlimit(10**6)
# N = int(input())

# A = [[0] * (2*N+1) for i in range(2*N+1)]


# for i in range(2*N-1):
#     c = list(map(int, input().split()))
#     for j in range(len(c)):
#         A[i+1][i+j+2] = c[j]
#         A[i+j+2][i+1] = c[j]

# ans = 0

# def dfs(selected,pairs):
#     global ans
#     if len(pairs) == 2*N:
#         tmp = 0
#         for i in range(0,2*N,2):
#             a,b = pairs[i],pairs[i+1]
#             x = A[a][b]
#             tmp^=x
#         ans = max(ans,tmp)

#     elif len(pairs) %2 == 0:
#         i = 1
#         while selected[i] == True:
#             i+=1
#         pairs.append(i)
#         selected[i] = True
#         dfs(selected,pairs)
#         pairs.pop()
#         selected[i] = False
#     else:
#         for i in range(1,2*N+1):
#             if selected[i] == False:
#                 pairs.append(i)
#                 selected[i] = True
#                 dfs(selected,pairs)
#                 pairs.pop()
#                 selected[i] = False



# selected = [False] * (2*N+1)
# pairs = []
# dfs(selected,pairs)

# print(ans)
