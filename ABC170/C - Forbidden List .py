






X,N = map(int,input().split())
A = list(map(int, input().split()))

s =set(A)
for i in range(100):
    num= X-i
    if num not in s:
        print(num)
        exit()
    num= X+i
    if num not in s:
        print(num)
        exit()


