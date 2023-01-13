



N,P,Q,R = map(int,input().split())


A = list(map(int, input().split()))

B = [0] * (N+1)

# [0, 1, 4, 6, 8, 10, 13, 14, 18, 21, 23]
# P = By-Bx,Q = Bz-By,R = Bw-Bz
# By = Bx +P,Bz = Bx +P + Q,Bw = Bx + P + Q + R

B[0] = 0
for i in range(len(A)):
    B[i+1] = B[i] + A[i]
Bset = set(B)
# for i in B:
#     Bset.add(i)

print(Bset)
for i in range(N):
    Bx = B[i]
    By = Bx +P
    Bz = Bx +P + Q
    Bw = Bx + P + Q + R
    if By in Bset and Bz in Bset and Bw in Bset:
        print("Yes")
        exit()
print("No")
