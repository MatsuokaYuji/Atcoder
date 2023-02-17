


# N>8なら必ず答えが存在
def solve():

    L = [[] for i in range(200)]

    N = int(input())

    A = list(map(int, input().split()))

    # print(L)

    if N>8:
        A = A[:8]
    M = len(A)

    for bit in range(1,1<<M):
        s = 0
        I = []
        for i in range(M):
            if (bit >>i) & 1:
                s+=A[i]
                I.append(i+1)
        re = s%200
        L[re].append(I)
    return L

def print_answer(L):
    for i in range(200):
        if len(L[i])>=2:
            B = L[i][0]
            C = L[i][1]
            B1 = [len(B)] + B
            C1 = [len(C)] + C
            print("Yes")
            print(*B1)
            print(*C1)
            return
    print("No")
    return

L = solve()
print_answer(L)
