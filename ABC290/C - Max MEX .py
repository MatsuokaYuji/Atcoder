








from collections import Counter

N,K = map(int,input().split())
A = list(map(int, input().split()))

s = set(A)
c = 0
for i in range(K):
	if i not in s:
		print(i)
	else:
		c+=1
print(c)



# C = Counter(A[:K])
# print(C)

# def mex(C):
#     for i in range(N+1):
#         if C[i] == 0:
#             return i

# ans = mex(C)

# for i in range(N-K):
#     C[A[i]] -=1
#     C[A[i+K]] +=1
#     if A[i] > ans and C[A[i]] == 0:
#         ans = A[i]
   
# print(ans)

