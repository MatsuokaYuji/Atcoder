








# 周期性
n,x,m = map(int,input().split())

R = [-1] *(m+1)
R[x] = 1
A = [0,x]
while True:
  a = A[-1]**2%m
  if R[a] ==-1:
    R[a] = len(A)
    A.append(a)
  else:
    B,C = A[:R[a]],A[R[a]:]
    break
# print(B,C)


if n<= len(B)-1:
  s = sum(B[:n+1])
else:
  s = sum(B)
  n-= len(B)
  k,l = n//len(C),n%len(C)
  s+= k*sum(C) + sum(C[:l+1])
print(s)

