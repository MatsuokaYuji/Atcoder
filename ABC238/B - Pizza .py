





N = int(input())


A = list(map(int, input().split()))

B = [0]

for i in A:
    for j in range(len(B)):
        tmp = (B[j]+i)%360
        B[j] = tmp
    if 0 not in B:
        B.append(0)
    B.sort()
B.append(360)
ans = 0

for i in range(len(B)-1):
    ans = max(ans, B[i+1]-B[i])
print(ans)
    