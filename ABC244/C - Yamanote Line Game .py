





N = int(input())

A = list(i for i in range(1,2*N+2))
B = []

while True:
    d = A.pop(0)
    print(d, flush=True)
    n = int(input())
    if n==0:
        exit()
    else:
        A.remove(n)
