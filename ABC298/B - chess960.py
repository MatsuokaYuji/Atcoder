

N = int(input())



A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
if A==B:
    print("Yes")
    exit()

# def rotate(X):
#     rotate_X = [[0] * N for i in range(N)]
#     for k in range(a):
#         for i in range(N):
#             for j in range(N):
#                 rotate_X[j][N+1-j] = A[i][j] 
#     return rotate_X

rotate = lambda A: [list(x)[::-1] for x in zip(*A)] 


for a in range(4):
    A = rotate(A)
    # print(A)
    flag = True
    # print(B,"a")


    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j]!=1:
                flag = False
    if flag:
        print("Yes")
        exit()
print("No")
