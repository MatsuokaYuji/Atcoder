





N = int(input())

A = list(map(int, input().split()))


Q = int(input())


queries = [input().split() for _ in range(Q)]



for q in queries:
  k = int(q[1])
  if q[0] =="1":
    A[k-1] = int(q[2])
  if q[0] =="2":
    print(A[k-1])
    
