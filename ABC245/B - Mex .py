




N = int(input())


A = list(map(int, input().split()))

b = set(A)

for i in range(2001):
  if i not in b:
    print(i)
    exit()