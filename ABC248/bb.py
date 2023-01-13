





A, B, K = map(int, input().split())

tmp = A
count = 0
if A ==B:
    print(0)
    exit()
while True:
  count+=1
  tmp = tmp*K
  if tmp>=B:
    print(count)
    exit()