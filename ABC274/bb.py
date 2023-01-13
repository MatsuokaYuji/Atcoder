




h,w = map(int,input().split())


A = []

for i in range(h):
    array = list(input())
    A.append(array)

print(A)

ans = []

for i in range(w):
    tmp = 0
    for j in range(h):
        if A[j][i] == "#":
            tmp+=1
    ans.append(str(tmp))

for i in range(w-1):
    print(ans[i] + " ", end = "")
print(ans[w-1])
