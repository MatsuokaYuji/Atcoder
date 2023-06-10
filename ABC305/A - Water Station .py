


N = int(input())


A = [i for i in range(0,105,5)]
# print(A)
a = 100
for i in range(len(A)):
    d = A[i]
    ans = abs(N-A[i])
    a = min(ans,a)
s = a+N
t = N-a
if s%5==0 or s==0:
    print(s)
else:
    print(t)
# print(s,t)


