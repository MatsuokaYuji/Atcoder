



def judge():
    N,K = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp_a = [False] * N
    dp_b = [False] * N
    dp_a[0] = True 
    dp_b[0] = True 

    for i in range(N-1):
        if dp_a[i]:
            dp_a[i+1] |= abs(A[i] - A[i + 1]) <= K
            dp_b[i+1] |= abs(A[i] - B[i + 1]) <= K
        if dp_b[i]:
            dp_a[i+1] |= abs(B[i] - A[i + 1]) <= K
            dp_b[i+1] |= abs(B[i] - B[i + 1]) <= K
    return dp_a[N-1] or dp_b[N-1]

print("Yes" if judge() else "No")