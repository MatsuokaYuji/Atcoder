


N = int(input())

A = []

for i in range(N):
    B = input()
    A.append(B)
# ['-WWW', 'L-DD', 'LD-W', 'LDW-']

for i in range(N):
    for j in range(N):
        if A[i][j] =="-":
            continue
        if A[i][j] =="W":
            if A[j][i] != "L":
                print("incorrect")
                exit()
        if A[i][j] == "D":
            if A[j][i] != "D":
                print("incorrect")
                exit()
        if A[i][j] == "L":
            if A[j][i] != "W":
                print("incorrect")
                exit()
print("correct")

